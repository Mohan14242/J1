pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                script {
                    def jsonContent = readFile 'package.json'
                    def package = new groovy.json.JsonSlurper().parseText(jsonContent)
                    def version = package.version
                    echo "Software version: $version"
                }
            }
        }
    }
}
