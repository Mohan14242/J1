pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Read package.json file and extract version
                    def package = readJSON(file: 'package.json')
                    def version = package.version
                    echo "Software version: $version"
                    
                    // You can perform further build steps using the version information
                    // For example:
                    // sh "npm install"
                    // sh "npm build"
                }
            }
        }
    }
}
