from forex_python.converter import CurrencyRates, RatesNotAvailableError
import requests

# Function to show available currencies
def show_currencies():
    currencies = [
        'Afghanistan (AFN)', 'Australia (AUD)', 'Algeria (DZD)', 'Argentina (ARS)', 'Armenia (AMD)',
        'Bangladesh (BDT)', 'Brazil (BRL)', 'Belgium (EUR)', 'Bulgaria (BGN)', 'Bahamas (BSD)',
        'India (INR)', 'Indonesia (IDR)', 'Iraq (IQD)', 'Ireland (EUR)', 'Israel (ILS)',
        'Japan (JPY)', 'Jamaica (JMD)', 'Jordan (JOD)', 'Jersey (GGP)', 'Juba (SDG)'
        # Add more countries as needed
    ]
    return currencies

# Function to get currency rate and convert
def convert_currency(from_currency, to_currency, amount):
    cr = CurrencyRates()
    
    try:
        # Try to fetch the exchange rate
        rate = cr.get_rate(from_currency, to_currency)
        return rate * amount
    except RatesNotAvailableError:
        print(f"Error: Exchange rate for {from_currency} to {to_currency} is not available.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Network issue occurred while fetching data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Main function
def main():
   
    # Full line separator and welcome message
    print("-" * 50)
    print("Welcome to the GURJAR Currency Converter Services!")
    print("-" * 50)
    
    currencies = show_currencies()
    print("Available currencies:")
    for idx, currency in enumerate(currencies, 1):
        print(f"{idx}. {currency}")
    
    try:
        # Get user input for from and to currencies by number
        from_currency_idx = int(input("Enter the number of the currency you want to convert from: ")) - 1
        to_currency_idx = int(input("Enter the number of the currency you want to convert to: ")) - 1
        
        # Ensure the input is valid
        if from_currency_idx < 0 or from_currency_idx >= len(currencies) or to_currency_idx < 0 or to_currency_idx >= len(currencies):
            print("Error: Invalid currency selection. Please try again.")
            return
        
        # Get the selected currencies
        from_currency = currencies[from_currency_idx].split('(')[-1][:-1].strip()  # Extract currency code (e.g., INR, USD)
        to_currency = currencies[to_currency_idx].split('(')[-1][:-1].strip()      # Extract currency code (e.g., INR, USD)
        
        # Print selected currencies
        print(f"You selected: {from_currency} to {to_currency}")
        
        # Get amount to convert
        amount = float(input(f"Enter the amount in {from_currency}: "))
        
        # Convert and display the result
        result = convert_currency(from_currency, to_currency, amount)
        
        if result is not None:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
        else:
            print("Currency conversion failed. Please try again later.")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for selection or amount.")
        
if __name__ == "__main__":
    main()
