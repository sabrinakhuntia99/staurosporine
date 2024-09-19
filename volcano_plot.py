import matplotlib.pyplot as plt

# set plot
plt.figure(figsize=(10, 8))
plt.scatter(df['Log2_Fold_Change'], df['-log10(p-value)'], color='gray', alpha=0.5)

#  dotted lines for significance thresholds
plt.axhline(y=1.3, color='blue', linestyle='--', linewidth=1)  # -log10(p-value) threshold
plt.axvline(x=-1, color='red', linestyle='--', linewidth=1)  # Log2 fold change threshold (down)

# graph labels
plt.xlabel('Log2 Fold Change')
plt.ylabel('-Log10(p-value)')
plt.title('Volcano Plot')
plt.legend(['-log10(p-value) = 1.3', 'log2(fold change) = -1'])
plt.tight_layout()

# save
plt.savefig('volcano_plot.png')
plt.show()
