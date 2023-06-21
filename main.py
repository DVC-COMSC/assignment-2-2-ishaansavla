def main():

    celcius = int(input("What is the temperature in celsius? "))
    fahrenheit = ((9/5)*(celcius)) + 32

    print('Fahrenheit: ' + format(fahrenheit, '.2f'))

    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
