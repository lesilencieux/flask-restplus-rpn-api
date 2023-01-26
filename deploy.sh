sudo docker stop flask_rpn_api
sudo docker rm flask_rpn_api
sudo docker rmi flask_rpn_api_img
sudo docker build -t flask_rpn_api_img .
sudo docker run -p 5001:5000 --name flask_rpn_api --restart always -d flask_rpn_api_img