pipeline {
    agent { node { label 'agent3'}}
    
    stages {
        stage('Build') {
            steps {
                // Your build steps here
                // For example, compile code, run tests, etc.
                sh '''
                pwd
                cd /home/centos/workspace/
                zip -r catalogue.zip sonar-pipeline/*

               '''
            }
        }
        stage('Upload to Nexus') {
            steps {
                script {
        
                    
                    // Nexus Artifact Uploader configuration
                    nexusArtifactUploader ( // This should match the ID defined in Jenkins configuration
                                          nexusVersion:"nexus3",
                                          protocol: 'http',
                                          nexusUrl: "23.23.22.187:8081/",
                                          credentialsId: "nexusCredentialsId",
                                          groupId: 'com.example', // Group ID of your artifacts
                                          version: '1.0.2', // Version of your artifacts
                                          repository: 'mohanproject', // Repository in Nexus where you want to upload artifacts
                                          artifacts: [
                                              [artifactId: 'mohanproject', file: 'J1.zip'] // Specify the artifact to upload and its location
                                          ]
                    )
                }

            }
        }
    }
   
}
