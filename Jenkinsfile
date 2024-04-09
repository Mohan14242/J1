pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Your build steps here
                // For example, compile code, run tests, etc.
                sh 'zip -r ./*' // Assuming Maven is used to build the project
            }
        }
        stage('Upload to Nexus') {
            steps {
                script {
        
                    
                    // Nexus Artifact Uploader configuration
                    nexusArtifactUploader ( // This should match the ID defined in Jenkins configuration
                                          nexusVersion:"nexus3"
                                          protocol: 'http',
                                          nexusUrl: "23.23.22.187:8081/",
                                          credentialsId: nexusCredentialsId,
                                          groupId: 'com.example', // Group ID of your artifacts
                                          version: '1.0.0', // Version of your artifacts
                                          repository: 'releases', // Repository in Nexus where you want to upload artifacts
                                          artifacts: [
                                              [artifactId: 'mohanproject', file: 'catalogue.zip'] // Specify the artifact to upload and its location
                                          ]
                    )
                }

            }
        }
    }
}
