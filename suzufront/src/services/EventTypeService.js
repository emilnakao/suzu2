import axios from 'axios'

class EventTypeService {



    get(searchToken){
        axios.get(`${}`)
    }
}

export default new EventTypeService()