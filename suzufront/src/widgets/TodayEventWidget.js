
import React, { Component } from 'react';
import CreateEventModal from "./CreateEventModal";
import SelectEventModal from "./SelectEventModal";

class TodayEventWidget extends Component {

    constructor(props){
        super(props)
        this.state = {event: {
                eventType: {
                  name: 'Dia Normal'
              }
            }
        }
    }

    render(){
        return (
            <div className="card my-2">
                <h5 className="card-header">Evento </h5>
                <div className="card-body text-center">
                    <h5 className="card-title">{this.state.event.eventType.name}</h5>
                    <p className="card-text">12/12/2019</p>

                </div>
                <div className="card-footer">
                    <button className="btn-sm btn-outline-dark float-left" data-toggle="modal" data-target="#selectEventModal">Eventos Passados</button>
                    <button className="btn-sm btn-outline-dark float-right" data-toggle="modal" data-target="#createEventModal">Evento de Hoje</button>
                </div>
                <CreateEventModal id={"createEventModal"}/>
                <SelectEventModal id={"selectEventModal"}/>
            </div>
        );
    }
}

export default TodayEventWidget