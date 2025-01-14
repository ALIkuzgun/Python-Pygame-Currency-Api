import pygame,requests

pygame.init()

width, height = 500, 330
ekran = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load('logo.png'))
pygame.display.set_caption('Ideal Weight Calculation')

input_text1 = ""
input_text1_alan = pygame.draw.rect(ekran,(255,255,2),(180,40,200,40),border_radius=15)
alan1 = 0
input_text2 = ""
input_text2_alan = pygame.draw.rect(ekran,(255,255,2),(180,100,200,40),border_radius=15)
alan2 = 0
input_text3 = ""
input_text3_alan = pygame.draw.rect(ekran,(255,255,2),(180,160,200,40),border_radius=15)
alan3 = 0

translate = 0
translate_alan = pygame.draw.rect(ekran,(255,255,2),(10,220,80,80),border_radius=15)

img = pygame.image.load('logo.png')

def doviz_cevirici():
    api_key = "API-KEY"  
    base_url = "https://v6.exchangerate-api.com/v6"

    kd = input_text1.strip()
    hd = input_text2.strip()
    try:
        m = float(input_text3.strip())
    except ValueError:
     
        print("Invalid amount entered. Please enter a valid number.")
        return

    try:
        url = f"{base_url}/{api_key}/pair/{kd}/{hd}"
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            kur = data["conversion_rate"]
            sonuc = m * kur
            result_text = f"{int(m)} {kd} = {sonuc:.2f} {hd}"
            text = pygame.font.Font(None, 52).render(result_text, True, (255, 255, 255))
            ekran.blit(text, (140, 250))
        else:
            print("Currency data could not be retrieved. Check the input values.")
    except Exception as e:
        print("An error occurred:", e)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RETURN:
                if alan1 == 1:
                   input_text1 = ""
                if alan2 == 1:
                   input_text2 = ""
                if alan3 == 1:
                   input_text3 = ""
            elif event.key == pygame.K_BACKSPACE:
                if alan1 == 1:
                  input_text1 = input_text1[:-1]
                if alan2 == 1:
                  input_text2 = input_text2[:-1]
                if alan3 == 1:
                  input_text3 = input_text2[:-1]
            else:
                if alan1 == 1:
                  if len(input_text1)<8:
                     input_text1 += event.unicode 
                if alan2 == 1:
                  if len(input_text2)<8:
                     input_text2 += event.unicode 
                if alan3 == 1:
                  if len(input_text3)<8:
                     input_text3 += event.unicode 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if input_text1_alan.collidepoint(mouse_pos):
                alan1 = 1
                alan2 = 0
                alan3 = 0
            if input_text2_alan.collidepoint(mouse_pos):
                alan2 = 1
                alan1 = 0
                alan3 = 0
            if input_text3_alan.collidepoint(mouse_pos):
                alan3 = 1
                alan1 = 0
                alan2 = 0
            if translate_alan.collidepoint(mouse_pos):
               translate = 1

    ekran.fill((32, 32, 32))  
    pygame.draw.rect(ekran,(255,255,255),(180,40,200,40),border_radius=15)
    pygame.draw.rect(ekran,(255,255,255),(180,100,200,40),border_radius=15)
    pygame.draw.rect(ekran,(255,255,255),(180,160,200,40),border_radius=15)
    pygame.draw.rect(ekran,(255,255,2),(10,220,80,80),border_radius=15)
    ekran.blit(img,(10,220))
    text = pygame.font.Font(None,42).render('1.Currency:', True, (255, 255, 255)) 
    ekran.blit(text, (10, 45))  
    text = pygame.font.Font(None,42).render('2.Currency:', True, (255, 255, 255)) 
    ekran.blit(text, (10, 105))  
    text = pygame.font.Font(None,42).render('Amount:', True, (255, 255, 255)) 
    ekran.blit(text, (10, 165))  
    text_input1 = pygame.font.Font(None,32).render(input_text1, True, (0, 0, 0)) 
    ekran.blit(text_input1, (190, 50))  
    text_input2 = pygame.font.Font(None,32).render(input_text2, True, (0, 0, 0)) 
    ekran.blit(text_input2, (190, 110))  
    text_input3 = pygame.font.Font(None,32).render(input_text3, True, (0, 0, 0)) 
    ekran.blit(text_input3, (190, 170)) 
    if translate == 1: 
      doviz_cevirici()
    pygame.display.flip()

pygame.quit()