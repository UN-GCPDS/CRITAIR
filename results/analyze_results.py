"""
CRITAIR Results Analysis Script
=============================

Script to analyze and visualize the BertScore evaluation results.
Generates summary statistics and comparative visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

def load_results():
    """Load all results CSV files."""
    results_dir = Path(__file__).parent / 'tables'
    
    unstructured = pd.read_csv(results_dir / 'unstructured_data_results.csv')
    structured = pd.read_csv(results_dir / 'structured_data_results.csv')
    recommendations = pd.read_csv(results_dir / 'recommendations_results.csv')
    
    return {
        'Unstructured': unstructured,
        'Structured': structured,
        'Recommendations': recommendations
    }

def generate_summary():
    """Generate summary statistics for all datasets."""
    results = load_results()
    
    print("🏆 CRITAIR - AI Models BertScore Evaluation Summary")
    print("=" * 60)
    
    for category, df in results.items():
        print(f"\n📊 {category} Data Analysis:")
        print("-" * 40)
        
        # Best performers
        best_bert = df.loc[df['BertScore'].idxmax()]
        fastest = df.loc[df['Inference Time'].idxmin()]
        best_balance = df.loc[df['Balance'].idxmin()]
        
        print(f"🎯 Best BertScore: {best_bert['Model']} ({best_bert['BertScore']:.4f})")
        print(f"⚡ Fastest Response: {fastest['Model']} ({fastest['Inference Time']:.2f}s)")
        print(f"⚖️  Best Balance: {best_balance['Model']} ({best_balance['Balance']:.2f})")
        
        # Summary statistics
        print(f"\n📈 Summary Statistics:")
        print(f"   • Average BertScore: {df['BertScore'].mean():.4f}")
        print(f"   • Average Time: {df['Inference Time'].mean():.2f}s")
        print(f"   • Average Balance: {df['Balance'].mean():.2f}")

def create_comparison_chart():
    """Create comparative visualization of all results."""
    results = load_results()
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('CRITAIR - AI Models Performance Comparison', fontsize=16, fontweight='bold')
    
    # BertScore comparison
    ax1 = axes[0, 0]
    categories = list(results.keys())
    models = results['Unstructured']['Model'].tolist()
    
    x = np.arange(len(models))
    width = 0.25
    
    for i, category in enumerate(categories):
        scores = results[category]['BertScore'].tolist()
        ax1.bar(x + i*width, scores, width, label=category, alpha=0.8)
    
    ax1.set_xlabel('Models')
    ax1.set_ylabel('BertScore')
    ax1.set_title('BertScore Comparison Across Categories')
    ax1.set_xticks(x + width)
    ax1.set_xticklabels(models, rotation=45, ha='right')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Inference Time comparison
    ax2 = axes[0, 1]
    for i, category in enumerate(categories):
        times = results[category]['Inference Time'].tolist()
        ax2.bar(x + i*width, times, width, label=category, alpha=0.8)
    
    ax2.set_xlabel('Models')
    ax2.set_ylabel('Inference Time (seconds)')
    ax2.set_title('Response Time Comparison')
    ax2.set_xticks(x + width)
    ax2.set_xticklabels(models, rotation=45, ha='right')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Balance scatter plot
    ax3 = axes[1, 0]
    colors = ['blue', 'red', 'green']
    for i, (category, df) in enumerate(results.items()):
        ax3.scatter(df['BertScore'], df['Inference Time'], 
                   label=category, alpha=0.7, s=100, c=colors[i])
        
        # Add model labels
        for idx, row in df.iterrows():
            ax3.annotate(row['Model'][:8], 
                        (row['BertScore'], row['Inference Time']),
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=8, alpha=0.7)
    
    ax3.set_xlabel('BertScore')
    ax3.set_ylabel('Inference Time (seconds)')
    ax3.set_title('Quality vs Speed Trade-off')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Balance ranking
    ax4 = axes[1, 1]
    all_balances = []
    all_labels = []
    all_categories = []
    
    for category, df in results.items():
        for idx, row in df.iterrows():
            all_balances.append(row['Balance'])
            all_labels.append(f"{row['Model'][:10]}")
            all_categories.append(category)
    
    # Sort by balance (lower is better)
    sorted_data = sorted(zip(all_balances, all_labels, all_categories))
    top_10 = sorted_data[:10]  # Top 10 best balance
    
    balances, labels, cats = zip(*top_10)
    colors_map = {'Unstructured': 'blue', 'Structured': 'red', 'Recommendations': 'green'}
    bar_colors = [colors_map[cat] for cat in cats]
    
    ax4.barh(range(len(labels)), balances, color=bar_colors, alpha=0.7)
    ax4.set_yticks(range(len(labels)))
    ax4.set_yticklabels(labels)
    ax4.set_xlabel('Balance Score (lower is better)')
    ax4.set_title('Top 10 Best Balance Models')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save chart
    output_path = Path(__file__).parent / 'reports' / 'bert_inference_comparison.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n📊 Comparison chart saved to: {output_path}")
    
    return fig

if __name__ == "__main__":
    print("🚀 Generating CRITAIR results analysis...")
    
    # Generate summary
    generate_summary()
    
    # Create visualizations
    create_comparison_chart()
    
    print("\n✅ Analysis complete!")
    print("📁 Check the 'reports' folder for generated visualizations.")