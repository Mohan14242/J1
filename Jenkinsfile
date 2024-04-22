def jsonContent
def version
def jsonData
pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                script {
                    jsonContent = readFile(file: 'package.json')
                    jsonData = readJSON text: jsonContent

// Access the version property
                    version = jsonData.'version'
                    echo "Version: ${version}"

                    
                    
                }
            }
        }
    }
}
