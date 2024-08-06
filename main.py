#from http import cookies
#from msilib.schema import ServiceControl
#from ssl import Options
from flask import Flask, request, redirect, render_template_string
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  



#from flask_cors import CORS, cross_origin
#from webdriver_manager.chrome import ChromeDriverManager  # Ayuda a gestionar el controlador

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solicitud de Servicios</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">
</head>
<body>
<style>
body, html {
    height: 100%;
    margin: 0;
    font-family: 'Poppins', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f2f5;
  }

  .login-container {
    background-color: #ffffff;
    padding: 20px 40px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 400px;
  }

  .login-container h2 {
    margin-bottom: 20px;
    font-size: 24px;
    font-weight: 500;
    text-align: center;
    color: #333333;
  }

  .login-container .input-group {
    margin-bottom: 15px;
  }

  .login-container .input-group label {
    display: block;
    font-weight: 500;
    margin-bottom: 5px;
    color: #555555;
  }

  .login-container .input-group input {
    width: 100%;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #cccccc;
    font-size: 16px;
    color: #333333;
  }

  .login-container .input-group input:focus {
    border-color: #007bff;
    outline: none;
  }

  .login-container .login-btn {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .login-container .login-btn:hover {
    background-color: #0056b3;
  }

  .login-container .forgot-password {
    text-align: center;
    margin-top: 15px;
  }

  .login-container .forgot-password a {
    color: #007bff;
    text-decoration: none;
  }

  .login-container .forgot-password a:hover {
    text-decoration: underline;
  }
</style>
    <div class="login-container">
    <h1>Solicitud</h1>
    <form action="/redirigir" method="POST">
        <div class="input-group">
            <label for="nombre">Nombre Completo:</label>
            <input type="text" id="nombre" name="nombre" required><br><br>  
        </div>
        <div class="input-group">
            <label for="id">Matrícula:</label>
            <input type="text" id="id" name="id" required><br><br>
        </div>
        <button type="submit" class="login-btn">Acceder a la plataforma</button>
    </form>
    </div>
</body>
</html>
    '''

@app.route('/redirigir', methods=['POST'])
def redirigir():
    nombre = request.form['nombre']
    id_estudiante = request.form['id']

  # Configurar Selenium para iniciar sesión en modo headless
    #options = Options()
    #options.headless = True
    # Configuracion privada (modificar después)
    #driver = webdriver.Chrome(service=ServiceControl(ChromeDriverManager().install()), options=options)
    driver = webdriver.Edge()
    driver.get("https://ventanillaingresospropiosvdos-qa.michoacan.gob.mx/")
    
    #try:

    driver.execute_script("""
            document.getElementById('usuario').type = 'password';
            document.getElementById('password').type = 'password';
        """)

    # Iniciar sesión
    driver.implicitly_wait(5)
    username_field = driver.find_element(By.ID, "usuario")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("IP_UCEMICH_VENTANILLA") #IPP_UCEMICH_VENTANILLA
    password_field.send_keys("y0e4C5.3*") #99FO#Mm*
    password_field.send_keys(Keys.RETURN)

    # Esperar la redirección después del login
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "#"))
    )

        # Extraer cookies de sesión
        #cookies = driver.get_cookies()
        #driver.quit()

    html_content = f"""
        <html>
        <head>
            <title>Redirigiendo...</title>
            <script type="text/javascript">
                window.location.href = "www.google.com";
            </script>
        </head>
        <body>
            <p>Redirigiendo, por favor espera...</p>
        </body>
        </html>
        """
    return render_template_string(html_content)


    """  except Exception as e:
        driver.quit()
        return f"Error: {str(e)}", 500 """ 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200)
