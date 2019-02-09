
import React, { Component } from 'react';
import TodayEventWidget from "../widgets/TodayEventWidget";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCheck } from '@fortawesome/free-solid-svg-icons'
import PresenceListWidget from "../widgets/PresenceListWidget";

import {HotKeys} from 'react-hotkeys';

const keyMap = {
    moveUp: 'up',
    moveDown: 'down'
}

class SelfCheckIn extends Component {

    constructor(props){
        super(props)
        this.state = {
            placeholderNome: "Digite seu nome aqui",
            nameNotFoundMsg: "Não encontrou seu nome? Aperte Enter para cadastrar.",
            outraRegionalMsg: "É de outra regional? Clique aqui",
            nameNotFound: false,
            suggestions: [
                {name: 'Emil Yoshigae Nakao'},
                {name: 'Lia Yoshigae Nakao'},
            ],
            focusIndex: 0
        }

        this.keyboardHandlers = {
            'moveUp': (event) => {
                let updatedState = {...this.state};
                if(updatedState.focusIndex > 0){
                    updatedState.focusIndex--;
                }
                this.setState(updatedState)
                console.log('up')
            },
            'moveDown' : (event) => {
                let updatedState = {...this.state};
                if(updatedState.focusIndex < (updatedState.suggestions.length - 1)){
                    updatedState.focusIndex++;
                }
                this.setState(updatedState)
                console.log('down')
            }
        };
    }

    render(){
        return (
            <HotKeys keyMap={keyMap} handlers={this.keyboardHandlers} role="main" class="container-fluid d-flex flex-fill bg-dark">
                <div className="flex-fill d-flex flex-row">
                    <div className="col-3 mr-n2 flex-fill d-flex flex-column">
                        <TodayEventWidget/>
                        <PresenceListWidget/>
                    </div>
                    <div className="flex-fill d-flex">
                        <div className="card mt-2 mb-2 mx-2 flex-fill">
                            <h5 className="card-header"><FontAwesomeIcon icon={faCheck}/> Marcar Presenças </h5>
                            <div className="card-body">
                                <input type="text" className="form-control form-control-lg mb-2" placeholder={this.state.placeholderNome} autoFocus={true}/>

                                {/* Caso nenhuma sugestão tenha sido encontrada, mostra msg */}
                                {this.state.nameNotFound &&
                                (<div>
                                    <div className="text-center v-100"><i>{this.state.nameNotFoundMsg}</i></div>

                                </div>)

                                }

                                {/* Lista de opções de nomes */}
                                {this.state.suggestions.map(function(suggestion, index){
                                    return <div className={"suzu-checkin-row rounded " + (index === this.state.focusIndex ? 'highlight' : '')} >
                                        <h4>{suggestion.name}</h4>
                                        <button class="btn btn-outline-secondary btn-sm" ng-click="editYokoshi(yokoshi)"><span class="fa fa-pencil text-warning"></span> Corrigir Cadastro</button>
                                        <button class="btn btn-outline-secondary btn-sm" ng-click="cancelPresence(yokoshi)" ng-disabled="!isYokoshiPresent(yokoshi)"><span class="fa fa-minus-square text-danger"></span> Cancelar Presença</button>
                                        <button class="suzu-checkin-row-presencebtn btn btn-success float-right my-auto" ng-disabled="isYokoshiPresent(yokoshi)" ng-click="togglePresence(yokoshi)"><span class="fa fa-check"></span> Marcar Presença</button>

                                    </div>;
                                }.bind(this))}

                                {/* Possibilita busca de yokoshi de outras regionais */}
                                <div className="text-center v-100"><i></i> <button className={"btn btn-primary"}>{this.state.outraRegionalMsg}</button></div>
                            </div>
                        </div>
                    </div>
                </div>
            </HotKeys>
        );
    }
}

export default SelfCheckIn