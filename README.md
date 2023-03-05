# API REST con Flask

En este template vamos a crear una api rest con flask. Para hacerlo más interesante, nuestra api nos devolverá los principales encabezados de las noticias presentes en distintos diarios del país.

## Entorno

Asegurarse de tener instalado `git` . Esto se puede revisar muy fácilmente a través del comando `git --version` . En caso de no estar instalado, se puede hacer a través de los siguientes paso

- En Linux, a través del comando `sudo apt install git`.
- En Windows, a través de la pagina oficial https://git-scm.com/

Tener actualizado `python` a la versión `lts`. Si desea asegurarse, puede ejecutar el comando `python --version` que le indicara la versión de `python` instalado en su sistema. Este debe ser `3.9` o superior. Si no esta instalado, puede obtener:

- En windows, desde Microsoft Store.
- En Linux, consulte en las fuentes oficiales de cada distro para actualizar `python` ya que este suele estar instalado por defecto.

Por último, instalar o actualizar `pipenv` como gestor de dependencias para este proyecto. Esto se puede hacer mediante el comando `pip install --user pipenv`. Para más información, visitar https://pipenv.pypa.io/en/latest/

## Instalación y ejecución

- 🛠Para instalar las dependencias ejecutar el siguiente comando `pipenv install` o `pip install -r requirements.txt`
- ⚒Para ejecutar el modo playground o repl, ejecutar el siguiente comando `pipenv run start`

## Rutas

- `/api/v1/news` : Devuelve en forma de arreglo, todas las noticias obtenidas de Clarín e Infobae
- `/api/v1/news?words=`: Devuelve en forma de arreglo, todas las noticias obtenidas de Clarín e Infobae que coincidan o contengan a las palabras sugeridas en `words`. Ejemplo: ‘`/api/v1/news?words=sismo`’ devolverá todas las noticias que contengan la palabra *sismo* en ellas.