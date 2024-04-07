pipeline{
    agent any
    stages{
        stage("build"){
            agent { label "agent1"}
            steps{
                sh '''
                ls -la'''

            }
        }
        stage("test"){
            agent { label "agent2" }
            steps{
               script{
                ls -la
               }
            }
        }
        stage("plan"){
            steps{
                echo "this is teh plan stage"
            }
        }
    }
}