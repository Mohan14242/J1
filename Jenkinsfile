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
                    version=jsonContent.'version'

                    
                    
                }
            }
        }
    }
}
