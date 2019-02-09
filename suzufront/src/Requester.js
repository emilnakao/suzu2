import axios from 'axios';

class Requester {
    BASE_URL = '/api'

    get(url){
        return axios.get(`${this.BASE_URL}/${url}`);
    }

    post(url, data){
        return axios.post(`${this.BASE_URL}/${url}`, data);
    }
}

export default new Requester();