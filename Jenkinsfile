pipeline {
    agent any  
    parameters{
        string(name: "param1", defaultValue: "default_value1", description: "Parameter 1 description")
        choice(name: "param2", choices: ["option1", "option2", "option3"], description: "Parameter 2 description")
        booleanParam(name: "param3", defaultValue: true, description: "Parameter 3 description")
    }
    stages{
        stage("testing the statge"){
            steps{
                script{
                    echo "the parameters are ${params.param1}"
                    echo "the second parameter is ${params.param2}"
                    echo "the thidrd parameters is ${params.param3}"

            }
            }
        }
    }
}