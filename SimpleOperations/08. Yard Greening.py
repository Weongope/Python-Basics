yard = float(input())

total_price = yard * 7.61

disc = total_price * 0.18
price = total_price - disc

print(f"The final price is: {price:.2f} lv.\nThe discount is: {disc:.2f} lv.")