pipeline {
    agent any
    environment {
        VERSION = '' // Define the version variable here (replace with actual version)
    }
    stages {
        stage('get the version') {
            steps {
                script {
                    def package = readJSON(file: "package.json")
                    def version = package.version // Store the version in a variable
                    echo "Software version: ${version}"
                }
            }
        }
        stage("printing the version") {
            steps {
                script {
                    def packageVersion = env.VERSION // Access the version from the environment
                    sh "echo 'The package version is ${packageVersion}'"
                }
            }
        }
    }
}
