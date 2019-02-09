import React from 'react';
import ReactDOM from 'react-dom';
import SelfCheckIn from "./SelfCheckIn";

it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<SelfCheckIn />, div);
    ReactDOM.unmountComponentAtNode(div);
});
