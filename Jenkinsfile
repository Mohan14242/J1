pipeline {
    agent any 
    environment {
        version = '' // Define the version variable here
    }
    stages {
        stage("getting the version of the file") {
            steps {
                script {
                    // Read package.json file and extract version
                    def package = readJSON(file: 'package.json')
                    def version = package.version // Store the version in the environment variable
                    echo "Software version: $version"
                }
            }
        }
        stage("printing the version") {
            steps {
                script {
                    // Access the version from the environment
                    def packageVersion = env.version
                    sh "echo 'The package version is ${packageVersion}'"
                }
            }
        }
    }
}
