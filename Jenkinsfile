pipeline {
    agent any  
    parameters{
        string(name:"mohan",value:"1.0.0")
    }
    stages{
        stage("testing the statge"){
            steps{
                script{
                    echo "the parameters are ${params.mohan}"
            }
            }
        }
    }
}