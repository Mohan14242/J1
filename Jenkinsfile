pipeline {
    agent { node { label "terraform1" } }
    environment {
        package = ''
    }
    stages {
        stage("getting the version of the file") {
            steps {
                script {
                    // Read package.json file and extract version
                    def package = readJSON file: "package.json"
                    version = package.version
                    echo "Software version: $version"
                }
            }
        }
        stage("printing the version") {
            steps {
                script {
                    // You need to define 'package' here or pass it from the previous stage
                    // If you want to use it across stages, you need to define it at the top level
                    def package = env.package
                    sh "echo 'The package version is ${package}'"
                }
            }
        }
    }
}
