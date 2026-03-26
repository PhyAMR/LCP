import matplotlib.cm as cm
import matplotlib.colors as mcolors

label_dict = {
    'optimizer': 'Optimizer',
    'regularizer': 'Regularizer',
    'dropout': 'Dropout Rate',
    'learning_rate': 'Learning Rate'
}

def results_plot(tuner, num_trials=None, column="regularizer", row="optimizer", 
                 hue="dropout", x_var="learning_rate", label_dict=label_dict, 
                 sig_figs=3, title=None):
    
    if num_trials is None:
        num_trials = len(tuner.oracle.trials)
    trials = tuner.oracle.get_best_trials(num_trials=num_trials)

    if title is None:
        title = f"Parameter search for a model with {len(tuner.oracle.trials)} trials"

    results_list = []
    for trial in trials:
        data = trial.hyperparameters.values.copy()
        data['val_accuracy'] = round(trial.score, 3) if trial.score is not None else 0
        results_list.append(data)
    
    df = pd.DataFrame(results_list)

    # 1. Handling Missing Columns (Safety for different models)
    for col in [column, row, hue, x_var]:
        if col is not None and col not in df.columns:
            df[col] = "N/A"
    global_max = df['val_accuracy'].max()
    # 2. Rounding Logic
    def round_df_to_sig_figs(df_in, n_sigs):
        df_numeric = df_in.select_dtypes(include=[np.number])
        vals = df_numeric.values
        mask = (vals != 0) & (~np.isnan(vals))
        log_10 = np.floor(np.log10(np.abs(np.where(mask, vals, 1))))
        decimals = (n_sigs - 1) - log_10
        rounded = np.where(mask, np.round(vals * 10**decimals) / 10**decimals, vals)
        df_in[df_numeric.columns] = rounded
        return df_in

    df = round_df_to_sig_figs(df, sig_figs)

    # 3. FacetGrid Setup with Hue Logic
    colormap = None
    norm = None
    
    if hue is not None and hue in df.columns and df[hue].nunique() > 1:
        if df[hue].nunique() <= 9:
            # Discrete Case
            g = sns.FacetGrid(df, col=column, row=row, margin_titles=True, height=4, hue=hue, palette="Set2")
        else:
            # Continuous Case (Fixing the Palette/Hue swap)
            norm = mcolors.Normalize(vmin=df[hue].min(), vmax=df[hue].max())
            colormap = cm.get_cmap("cubehelix")
            unique_hues = sorted(df[hue].unique())
            palette_dict = {val: mcolors.to_hex(colormap(norm(val))) for val in unique_hues}
            
            # FIXED: hue is the COLUMN NAME, palette is the DICTIONARY
            g = sns.FacetGrid(df, col=column, row=row, margin_titles=True, height=4, hue=hue, palette=palette_dict)
    else:
        g = sns.FacetGrid(df, col=column, row=row, margin_titles=True, height=4)

    # 4. Annotate Function
    
    def annotate_scores(data, **kws):
        if data.empty:
            return
            
        ax = plt.gca()
        # 1. Identify which variable is on the y-axis
        # In your logic, this is either x_var or the 'groups_of' binned column
        y_var_name = (x_var if df[x_var].unique().shape[0] <= 10 else f"groups_of_{x_var}")
        
        # 2. Find the row with the maximum accuracy in THIS facet
        best_row_idx = data['val_accuracy'].argmax()
        max_score = data['val_accuracy'].iloc[best_row_idx]
        best_y_label = data[y_var_name].iloc[best_row_idx]
        
            
        # 3. Get the vertical position of that specific category
        # Matplotlib's categorical axes use integers 0, 1, 2... for positions
        
        # We find where our 'best_y_label' sits in the current y-ticks
        # A more robust way is using the category index from the plot
        y_pos = None
        ticks = ax.get_yticks()
        labels = [t.get_text() for t in ax.get_yticklabels()]
        
        try:
            # Match the label string to find the correct tick index
            label_idx = labels.index(str(best_y_label))
            y_pos = ticks[label_idx]
        except (ValueError, IndexError):
            # Fallback to middle if label matching fails
            y_pos = 0.5 
            transform = ax.transAxes
        else:
            # If we found the tick, we use Data coordinates for Y and Axes for X
            transform = ax.get_yaxis_transform() 

        # 4. Draw the text inside the bar or at the end of it
        if max_score < global_max:
            ax.text(0.95, y_pos, f"Score: {max_score:.3f}", 
                    transform=transform, 
                    fontsize=9, fontweight='bold',
                    ha='right', va='center', 
                    color=kws.get('color', 'black'),
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
        else:
            ax.text(0.95, y_pos, f"Score: {max_score:.3f}", 
                transform=transform, 
                fontsize=9, fontweight='bold',
                ha='right', va='center', 
                color=kws.get('color', 'black'),
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.2'))

    # 5. Plotting
    y_axis_var = x_var if x_var in df.columns else df.columns[0]
    
    if df[x_var].unique().shape[0] <= 10:  # Only annotate if there are 10 or fewer unique x values

        g.map_dataframe(
            sns.barplot,
            x="val_accuracy",
            y=y_axis_var,
            errorbar=None,
            orient="h"
            
        )
    else:
        df[f'groups_of_{x_var}'] = pd.cut(df[x_var], bins=10, duplicates='drop')
        g.map_dataframe(
            sns.barplot,
            x="val_accuracy",         # Numbers go on X
            y=f'groups_of_{x_var}',   # Categories go on Y
            errorbar=None,
            orient="h"                # Use "h" for clarity, or leave it to auto-detect
        )
    g.map_dataframe(annotate_scores)

    # 6. Final Layout and Margin Title Fixes
    # Push right margin to make room for titles
    g.fig.subplots_adjust(right=0.8, top=0.85, wspace=0.4) 
    g.fig.suptitle(title, fontsize=14, fontweight='bold')
    g.set_titles(col_template=f"{column}="+"{col_name}", row_template=f"{row}="+"{row_name}", fontweight='bold')

    # FIX: Reposition Row Titles to the far right
    for txt in g.fig.texts:
        if txt.get_rotation() == -90:
            txt.set_x(0.92) # Absolute figure coordinate
            txt.set_va('center')

    # Add Colorbar for Continuous Hue
    if colormap and norm:
        sm = plt.cm.ScalarMappable(cmap=colormap, norm=norm)
        sm.set_array([])
        cbar_ax = g.fig.add_axes([0.85, 0.15, 0.02, 0.6]) # [left, bottom, width, height]
        g.fig.colorbar(sm, cax=cbar_ax, label=label_dict.get(hue, hue))
    else:
        
        g.add_legend()
    g.set(xlim=(0, 1.1)) 
    plt.show()