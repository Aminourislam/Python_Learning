def calculate_bmi(weight, height):
	weight = (weight*0.4535923) #kg
	height = height * 0.0254 #m

	bmi = weight/height**2
	print(round(bmi, 1))

	return bmi

calculate_bmi(180, 70) # 25.8.
calculate_bmi(140, 64) # 24.0.
calculate_bmi(160, 76) # 19.5.
calculate_bmi(200, 60) # 39.1.
calculate_bmi(150, 68) # 22.8.
