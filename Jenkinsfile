def jsonContent
pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                script {
                    jsonContent = readFile(file:'package.json')
                     def version=jsonContent['version']
                    
                    
                }
            }
        }
    }
}
