set -x

echo "$data-set"
sudo apt-get -y update
cur_dir=$(pwd)
data_dir=$cur_dir/model_data
mkdir -p $data_dir
wget -P $data_dir https://www.baoshuanglong.com/zb_users/upload/2020/03/202003241585013033482253.jpg

python3 main.py
