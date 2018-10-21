Website: https://gmcjeyzer.wixsite.com/growth/


## Inspiration

Garbage is one of the major issues in the world. People unrealistically expect waste collectors to gather garbage when the ratio of garbage being thrown on the ground is higher than that of being collected. If we can somehow involve EVERYONE, not just the workers, we can really push the world forward.

A way to be motivated to do a good deed (other than the feeling of satisfaction in helping live in a better environment) is to find an instant return that would help you in some critical way. This is where this idea comes to life. The high-level view is as simple as we ask people (homeless or anyone) to help gather garbage and in return, they get some kind of credit/points that (when accumulated) can help with the following (and more):

1) Buying food/clothes
2) Getting themselves or their kids to school
3) Getting cheaper Healthcare/Medicine

So now we don't just help the environment, but the homeless and people in need as well. You could also donate your points to other people in need and by doing so you're now donating your **time not your money to help others**.

## What it does

Gaining points can be done through an application or as simple as scanning your ID/face depending on the weight of the garbage bags you collect. But this is a specific use case, this could be expanded to any community service: Planting trees/Shoveling snow/Mowing the lawn.

Over time, our application will also start analyzing how well certain people are doing and therefore start recommending them for actual jobs. This way businesses have a record and have confidence in the recommended people.

## How we built it

We separated our tasks. One person worked on the backend and the visual recognition using Python. Two members worked on the front end of the application using Wix.com. Our fourth member worked on connecting the front end with the back end and therefore creating API endpoints and making sure everything fits together in a good way.

## Challenges we ran into

Although Wix.com has fantastic templates and is very easy to use, it is very limited for hardcore programmers. For instance, we required the website to open webcam and take a snapshot and send that picture to the backend for visual recognition. Wix does not support browser cam. Therefore, for demo purposes, we had to create an API endpoint in Python, and when it's reached it runs a Python script that accesses the local camera, takes a snapshot, sends it to Google's AutoML Visual Recognition and send the result back to the website.

We also tried to demonstrate weighing the garbage bags. We checkout out an Adruino and it's kit but we were looking for a pressure sensor but there wasn't any; so then we thought of getting four springs and a sheet with an ultrasound sensor on the ground to measure how far the sheet is from the ground. The Adruino was out of date and we tried to update it but quickly recognized that we would waste time trying to make it work, therefore discsarded using the Adruino. We also tried using Qualcomm's hardware but had no luck.

## Accomplishments that we're proud of

1) We were able to create a frontend that we are proud of
2) We managed to not hardcode a lot of stuff and actually used a database
3) We managed to train Google's AutoML and got an accuracy of 0.88+.
4) We managed to split tasks and collaborate in a neat way.

## What we learned

## What's next for Growth

Growth's next steps are very apparent. We aim to help the world and so we will begin with implementing the garbage collection and bringing it to life. We would set up one or two stations and test this out at events where clean up is needed. If that goes well we start expanding to places that do require garbage to be collected. In parallel, we would be working to provide other important community services.
