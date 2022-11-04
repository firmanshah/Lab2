def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi=weight/(height*height)
    if (bmi < 18.5):{
        print("You are underweight")
    } 
    elif (bmi > 25):{
        print("You are overweight")
    }
    else :{
        print("You are normal")
    }

calculate_bmi(weight=57, height=1.73)