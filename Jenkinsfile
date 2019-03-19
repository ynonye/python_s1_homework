node('slave1'){
    currentBuild.result = "SUCCESS"
    stage('Printing hello world'){
        sh 'echo "Hello World"'
    }
    {
    stage('fail'){
        sh 'exit 1'
    }    
    stage('deploy ok'){
        sh 'echo "deploy ok"'        
    }
}
