import sys
import subprocess



def check_node_status(node_name):
	cmd = "wget https://www.rioaliancafrancesa.com.br/captacao/wp-content/uploads/2018/06/piste-002.mp3"
	return 	subprocess.check_output(cmd, shell=True)


