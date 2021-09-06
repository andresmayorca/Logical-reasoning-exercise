#Shirt One
class shirtOne:
    def characteristicsShirts(shirtColor, circlesColor, amountCircles):
        shirtColor = green
        circlesColor = blue
        amountCircles = 5    

#Shirt Two
class shirtTwo:
    def characteristicsShirts(ShirtColor, colorCircles, amountCircles):
        ShirtColor = blue
        colorCircles = grazed 
        amountCircles = 8

#Shirt Three  
class shirtThree:
    def characteristicsShirts(shirtColor, colorCircles, amountCircles):
        shirtColor = yellow
        colorCircles = orange
        amountCircles = 4

# Shirt Four
class shirtFour:
    def characteristicsShirts(shirtColor, colorCircles, amountCircles):
        shirtColor = orange
        colorCircles = green
        amountCircles = 3

indexOne = shirtTwo
indexTwo = shirtFour
indexThree = shirtOne
indexFour = shirtThree

if indexOne == shirtTwo:
    print("""
    Characteristics of the Shirt:
    Color = Blue,
    Number of circles = 8
    Color Circles = Grazed    
    """)
    
if indexTwo == shirtFour:
    print("""
    Characteristics of the Shirt:
    Color = Orange,
    Number of circles = 3
    Color Circles = Green
    """)

if indexThree == shirtOne:
    print("""
    Characteristics of the Shirt:
    Color = Green,
    Number of circles = 5
    Color Circles = Blue
    """)
if indexFour == shirtThree:
    print("""
    Characteristics of the Shirt:
    Color = Yellow,
    Number of circles = 4
    Color Circles = Orange
    """)
