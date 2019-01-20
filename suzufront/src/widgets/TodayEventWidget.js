
import React, { Component } from 'react';

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
                <div class="card-footer">
                    <a href="#" class="btn-sm btn-secondary float-left">Eventos Passados</a>
                    <a href="#" class="btn-sm btn-secondary float-right">Evento de Hoje</a>
                </div>
            </div>
        );
    }
}

export default TodayEventWidget