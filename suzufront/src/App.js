import $ from 'jquery';
import Popper from 'popper.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import './App.css';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome, faCheck, faMapMarkerAlt, faUserAlt } from '@fortawesome/free-solid-svg-icons'
import Home from "./pages/Home";
import SelfCheckIn from "./pages/SelfCheckIn";

class App extends Component {
  render() {
    return (
        <Router>
            <div className={"w-100 vh-100"}>
                <nav class="navbar navbar-expand-md navbar-dark bg-dark">
                    {/* Logo */}
                    <a class="navbar-brand" href="#"><b>SUZU</b>2</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    {/* Links */}
                    <div class="collapse navbar-collapse" id="navbarLinkSection">
                        <ul class="navbar-nav mr-auto">
                            <li class="nav-item active">
                                <a class="nav-link" href="/"><FontAwesomeIcon icon={faHome}/> Home <span class="sr-only">(current)</span></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Admin</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/selfCheckIn"><FontAwesomeIcon icon={faCheck}/> Marcar Presenças</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/okiyome"><FontAwesomeIcon icon={faCheck}/> Okiyome</a>
                            </li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="operationDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Operações</a>
                                <div class="dropdown-menu" aria-labelledby="operationDropdown">
                                    <a class="dropdown-item" href="#">Atualização de Cadastro</a>
                                    <a class="dropdown-item" href="#">Atualização de Núcleo</a>
                                </div>
                            </li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="operationDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Relatórios</a>
                                <div class="dropdown-menu" aria-labelledby="operationDropdown">
                                    <a class="dropdown-item" href="#">Presenças por Evento</a>
                                    <a class="dropdown-item" href="#">Presenças por Kumite</a>
                                    <a class="dropdown-item" href="#">Presenças por Mi-Kumite</a>
                                </div>
                            </li>
                        </ul>
                    </div>

                    {/* Session Info */}
                    <div class="float-right" id="navbarSessionSection">
                        <ul class="navbar-nav mr-auto">
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="regionalDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><FontAwesomeIcon icon={faMapMarkerAlt}/> Pinheiros</a>
                                <div class="dropdown-menu" aria-labelledby="regionalDropdown">
                                    <a class="dropdown-item" href="#">Trocar Regional</a>
                                </div>
                            </li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="userDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><FontAwesomeIcon icon={faUserAlt}/> Admin</a>
                                <div class="dropdown-menu" aria-labelledby="userDropdown">
                                    <a class="dropdown-item" href="#">Logout</a>
                                </div>
                            </li>
                        </ul>
                    </div>

                </nav>
                <div className="d-flex w-100 h-100 v-80">
                    <Route exact path="/" component={Home} />
                    <Route exact path="/selfCheckIn" component={SelfCheckIn} />
                    <Route exact path="/okiyome" component={SelfCheckIn} />
                </div>
            </div>

        </Router>
    );
  }
}

export default App;
