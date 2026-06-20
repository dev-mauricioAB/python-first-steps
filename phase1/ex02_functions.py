def classify_temperature(temp: float):
  if temp < 15:
    return 'Cold'
  if temp <= 28  & temp >= 15:
    return 'Comfortable'
  return 'Hot'

value = classify_temperature(20)

print(value)