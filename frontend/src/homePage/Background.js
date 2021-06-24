import React from "react";
import Particles from "react-particles-js";
import { makeStyles } from "@material-ui/styles";

const useStyles = makeStyles((theme) => ({
  body: () => ({
    height: "100%",
    width: "100%",
    zIndex: -10,
  }),
}));

export default function Background() {
  const classes = useStyles();
  return (
    //Continually monitor the number of particles to prevent lag
    <Particles
      className={classes.body}
      id="particles-js"
      params={{
        particles: {
          number: {
            value: 80,
            density: {
              enable: true,
              value_area: 700,
            },
          },
          color: {
            value: "#0000",
          },
          opacity: {
            value: 0.5,
            anim: {
              enable: true,
            },
          },
          size: {
            value: 3,
            random: true,
            anim: {
              enable: true,
              speed: 3,
            },
          },
          line_linked: {
            enable: true,
            color: "#8c8c8c", //light grey
          },
          move: {
            speed: 1.2,
            out_mode: "out",
            bounce: true,
          },
        },
        interactivity: {
          events: {
            // onhover: {
            //   enable: true,
            //   mode: "repulse",
            // },
            onclick: {
              enable: true,
              mode: "push",
            },
            resize: true,
          },
          modes: {
            push: {
              particles_nb: 1,
            },
            // repulse: {
            //   distance: 50,
            //   duration: 0.4,
            // },
          },
        },
      }}
    ></Particles>
  );
}
