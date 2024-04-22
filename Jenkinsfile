pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                script {
                    def p = readJSON file: 'package.json'
                    def version = p.version
                    echo "Software version: $version"
                }
            }
        }
    }
}
