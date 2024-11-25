from requests_html import HTMLSession

def recargar_pagina_con_requests_html(url, num_recargas):
    session = HTMLSession()
    
    print(f"\nIniciando recargas de {url}")
    print("=" * 50)

    for i in range(num_recargas):
        try:
            response = session.get(url)
            
            response.html.render()
            
            print(f"Recarga {i+1}/{num_recargas}: ÉXITO")
        except Exception as e:
            print(f"Recarga {i+1}/{num_recargas}: ERROR - {str(e)}")

    session.close()

if __name__ == "__main__":
    url = input("Introduce la URL (incluyendo https://): ").strip()
    num_recargas = int(input("Introduce el número de recargas: "))
    recargar_pagina_con_requests_html(url, num_recargas)