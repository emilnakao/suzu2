import axios from 'axios'
import Requester from "./Requester";

it('forwards get calls completing the url', () => {
    const spy = jest.spyOn(axios, 'get').mockImplementation(() => Promise.resolve({ success: true }));
    Requester.get('data')

    expect(spy).toHaveBeenCalledWith(`${Requester.BASE_URL}/data`);
});

it('forwards post calls completing the url', () => {
    const spy = jest.spyOn(axios, 'post').mockImplementation(() => Promise.resolve({ success: true }));
    let postData = {information:'xyz'}
    Requester.post('data', postData )

    expect(spy).toHaveBeenCalledWith(`${Requester.BASE_URL}/data`, postData);
});