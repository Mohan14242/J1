pipeline {
    agent any  
    parameters{
        string(name: "mohan", defaultValue: "1.0.0", description: "Version number")
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