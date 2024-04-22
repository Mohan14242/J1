def jsonContent
def version
pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                script {
                    jsonContent = readFile(file:'package.json')
                    echo " ${jsonContent.version}"
                    
                }
            }
        }
    }
}
