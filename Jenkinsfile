pipeline{
    agent { node{ lable 'agent1'}}
    stages{
        stage("test stage"){
            steps{
                script{
                    sh 'ls -la'
                }
            }
        }
    }
}