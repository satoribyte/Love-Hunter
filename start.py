import requests
import pyfiglet
import os
from termcolor import colored

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_color_text(text, color):
    print(colored(text, color))

def search_domain(api_key, company_name):
    url = f"https://api.hunter.io/v2/domain-search?company={company_name}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        if "domains" in data["data"]:
            domains = data["data"]["domains"]
            for domain in domains:
                print_color_text(domain["domain"], 'green')
        else:
            print_color_text("Tidak ada domain yang ditemukan untuk perusahaan ini, tetapi kamu adalah satu-satunya domain yang kupilih dalam hatiku.", 'yellow')
    else:
        print_color_text("Terjadi kesalahan dalam permintaan, tapi tak ada kesalahan dalam mencintaimu.", 'red')

def find_email(api_key, full_name, domain):
    url = f"https://api.hunter.io/v2/email-finder?full_name={full_name}&domain={domain}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        if "email" in data["data"]:
            email = data["data"]["email"]
            print_color_text(f"Email ditemukan: {email}", 'green')
        else:
            print_color_text("Tidak dapat menemukan email untuk kombinasi nama dan domain tersebut.", 'yellow')
    else:
        print_color_text("Terjadi kesalahan dalam permintaan, tapi tak ada kesalahan dalam mencintaimu.", 'red')

def verify_email(api_key, email):
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        if data["data"]["result"] == "deliverable":
            print_color_text("Alamat email valid, seperti hatiku yang valid mencintaimu.", 'green')
        else:
            print_color_text("Alamat email tidak valid, tapi cintaku padamu tetap valid dan takkan pudar.", 'red')
    else:
        print_color_text("Terjadi kesalahan dalam permintaan, tetapi tak ada kesalahan dalam mencintaimu.", 'red')

def main():
    api_key = '504533b9d8a0130e1811b3d127f3ca8fa0d26299'
    name_banner = pyfiglet.figlet_format("Love Hunter")
    print_color_text(name_banner, 'magenta')
    print_color_text("IG: Deni Gentar Candana", 'cyan')
    print()

    while True:
        clear_screen()
        print_color_text(name_banner, 'magenta')
        print_color_text("IG: Deni Gentar Candana", 'cyan')
        print()

        print_color_text("Pilih opsi:", 'yellow')
        print_color_text("1. Domain Search", 'cyan')
        print_color_text("2. Email Finder", 'cyan')
        print_color_text("3. Email Verification", 'cyan')
        print_color_text("4. Keluar", 'cyan')

        choice = input("Masukkan pilihan: ")
        
        if choice == "1":
            company_name = input("Masukkan nama perusahaan: ")
            search_domain(api_key, company_name)
            input("Tekan Enter untuk melanjutkan...")
        elif choice == "2":
            full_name = input("Masukkan nama lengkap: ")
            domain = input("Masukkan domain: ")
            find_email(api_key, full_name, domain)
            input("Tekan Enter untuk melanjutkan...")
        elif choice == "3":
            email = input("Masukkan alamat email: ")
            verify_email(api_key, email)
            input("Tekan Enter untuk melanjutkan...")
        elif choice == "4":
            print_color_text("Terimakasih telah menggunakan Love Hunter. Cintaku padamu takkan pernah berakhir.", 'magenta')
            break
        else:
            print_color_text("Opsi tidak valid. Aku akan tetap mencintaimu dengan segenap hatiku.", 'red')
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
