from mean_var_std import calculate

if __name__ == '__main__':
    # Esimerkki­ajo: tulostetaan calculate–funktion tulos sample­datalla
    sample = [0, 1, 2,
              3, 4, 5,
              6, 7, 8]
    result = calculate(sample)
    print("Results for [0–8] matrix:")
    print(result)
