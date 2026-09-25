#subplot
import matplotlib.pyplot as plt


# Create data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

# --- 1st Plot ---
plt.subplot(2, 1, 1)     # (2 rows, 1 column, 1st plot)
plt.plot(x, y1, color='blue')
plt.title("Square Numbers")  # Title for first plot

# --- 2nd Plot ---
plt.subplot(2, 1, 2)     # (2 rows, 1 column, 2nd plot)
plt.plot(x, y2, color='red')
plt.title("Reverse Squares") # Title for second plot

# Adjust layout
plt.tight_layout()  # Avoids overlapping of titles and labels
plt.show()
