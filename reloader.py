from requests_html import HTMLSession
import time
from datetime import datetime
import sys
from typing import Optional

class WebReloader:
 def __init__(self, url: str, num_reloads: int):
     self.url = url
     self.num_reloads = num_reloads
     self.session = HTMLSession()
     self.successful_reloads = 0
     self.failed_reloads = 0
     self.start_time = None

 def validate_url(self) -> bool:
     """Validate if the URL starts with http:// or https://"""
     return self.url.startswith(('http://', 'https://'))

 def print_progress(self, current: int, status: str, error: Optional[str] = None) -> None:
     """Print progress of the reloading process"""
     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     progress = f"[{current}/{self.num_reloads}]"
     
     if status == "SUCCESS":
         print(f"{timestamp} {progress} ✅ Success")
     else:
         print(f"{timestamp} {progress} ❌ Error: {error}")

 def print_summary(self) -> None:
     """Print summary of the reloading process"""
     elapsed_time = time.time() - self.start_time
     print("\n" + "=" * 50)
     print("SUMMARY")
     print("=" * 50)
     print(f"Total reloads attempted: {self.num_reloads}")
     print(f"Successful reloads: {self.successful_reloads}")
     print(f"Failed reloads: {self.failed_reloads}")
     print(f"Success rate: {(self.successful_reloads/self.num_reloads)*100:.2f}%")
     print(f"Total time elapsed: {elapsed_time:.2f} seconds")
     print("=" * 50)

 def reload_page(self) -> None:
     """Main function to reload the page"""
     if not self.validate_url():
         print("Error: Invalid URL. Please include http:// or https://")
         return

     print(f"\nStarting reloads for: {self.url}")
     print("=" * 50)
     
     self.start_time = time.time()

     try:
         for i in range(self.num_reloads):
             try:
                 response = self.session.get(self.url)
                 response.html.render(timeout=20)  # Added timeout parameter
                 self.successful_reloads += 1
                 self.print_progress(i + 1, "SUCCESS")
                 
             except Exception as e:
                 self.failed_reloads += 1
                 self.print_progress(i + 1, "ERROR", str(e))
             
             # Add a small delay between requests to prevent overloading
             time.sleep(1)

     except KeyboardInterrupt:
         print("\nProcess interrupted by user")
     
     finally:
         self.session.close()
         self.print_summary()

def get_valid_number() -> int:
 """Get and validate number of reloads from user"""
 while True:
     try:
         num = int(input("Enter number of reloads (1-1000): "))
         if 1 <= num <= 1000:
             return num
         print("Please enter a number between 1 and 1000")
     except ValueError:
         print("Please enter a valid number")

def main():
 try:
     url = input("Enter URL (including https://): ").strip()
     num_reloads = get_valid_number()
     
     reloader = WebReloader(url, num_reloads)
     reloader.reload_page()

 except Exception as e:
     print(f"An unexpected error occurred: {str(e)}")
     sys.exit(1)

if __name__ == "__main__":
 main()