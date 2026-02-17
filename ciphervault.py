#!/usr/bin/env python3
"""
Caesar Cipher Encryption and Decryption Program
Created for Internship Project
A comprehensive implementation of the Caesar Cipher algorithm with user-friendly interface
"""

class CaesarCipher:
    """
    A class to handle Caesar Cipher encryption and decryption operations.
    Supports both uppercase and lowercase letters, preserving non-alphabetic characters.
    """
    
    def __init__(self):
        self.alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    
    def encrypt(self, message: str, shift: int) -> str:
        """
        Encrypt a message using Caesar Cipher with the given shift value.
        
        Args:
            message (str): The message to encrypt
            shift (int): The shift value (positive integer)
            
        Returns:
            str: The encrypted message
        """
        encrypted = []
        
        for char in message:
            if char.isupper():
                # Handle uppercase letters
                index = self.alphabet_upper.find(char)
                if index != -1:
                    new_index = (index + shift) % 26
                    encrypted.append(self.alphabet_upper[new_index])
                else:
                    encrypted.append(char)
            elif char.islower():
                # Handle lowercase letters
                index = self.alphabet_lower.find(char)
                if index != -1:
                    new_index = (index + shift) % 26
                    encrypted.append(self.alphabet_lower[new_index])
                else:
                    encrypted.append(char)
            else:
                # Keep non-alphabetic characters unchanged
                encrypted.append(char)
        
        return ''.join(encrypted)
    
    def decrypt(self, encrypted_message: str, shift: int) -> str:
        """
        Decrypt a message using Caesar Cipher with the given shift value.
        
        Args:
            encrypted_message (str): The message to decrypt
            shift (int): The shift value used for encryption
            
        Returns:
            str: The decrypted message
        """
        # Decryption is just encryption with negative shift
        return self.encrypt(encrypted_message, -shift)
    
    def brute_force_decrypt(self, encrypted_message: str) -> list:
        """
        Attempt to decrypt a message by trying all possible shift values (1-25).
        
        Args:
            encrypted_message (str): The message to decrypt
            
        Returns:
            list: List of tuples containing (shift_value, decrypted_message)
        """
        possibilities = []
        
        for shift in range(1, 26):
            decrypted = self.decrypt(encrypted_message, shift)
            possibilities.append((shift, decrypted))
        
        return possibilities


def get_valid_shift():
    """
    Get a valid shift value from user input.
    
    Returns:
        int: Valid shift value
    """
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("🔐 CAESAR CIPHER ENCRYPTION & DECRYPTION 🔐")
    print("="*60)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute force decrypt (try all possible shifts)")
    print("4. Exit")
    print("="*60)


def main():
    """Main program function with interactive menu."""
    cipher = CaesarCipher()
    
    print("🎓 Welcome to the Caesar Cipher Program!")
    print("This program demonstrates the classic Caesar Cipher algorithm.")
    print("Perfect for learning about basic cryptography concepts.\n")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                # Encryption
                print("\n--- ENCRYPTION MODE ---")
                message = input("Enter the message to encrypt: ")
                shift = get_valid_shift()
                
                encrypted = cipher.encrypt(message, shift)
                print(f"\n✅ Original message: {message}")
                print(f"🔑 Shift value: {shift}")
                print(f"🔒 Encrypted message: {encrypted}")
                
            elif choice == '2':
                # Decryption
                print("\n--- DECRYPTION MODE ---")
                message = input("Enter the message to decrypt: ")
                shift = get_valid_shift()
                
                decrypted = cipher.decrypt(message, shift)
                print(f"\n🔒 Encrypted message: {message}")
                print(f"🔑 Shift value: {shift}")
                print(f"✅ Decrypted message: {decrypted}")
                
            elif choice == '3':
                # Brute force decryption
                print("\n--- BRUTE FORCE DECRYPTION MODE ---")
                message = input("Enter the encrypted message: ")
                
                possibilities = cipher.brute_force_decrypt(message)
                print(f"\n🔍 Trying all possible shift values for: {message}")
                print("-" * 60)
                
                for shift, decrypted in possibilities:
                    print(f"Shift {shift:2d}: {decrypted}")
                
                print("-" * 60)
                print("💡 Look for the shift value that produces meaningful text!")
                
            elif choice == '4':
                # Exit
                print("\n👋 Thank you for using the Caesar Cipher Program!")
                print("Hope you learned something about cryptography! 🎓")
                break
                
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("Please try again.")
        
        # Ask user if they want to continue
        if choice != '4':
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    # Run the program
    main()
