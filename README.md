# Factorio-RAM-builder

This hastily coded Python script creates a json file containing the constant combinators needed for addressing by each memory cell of my expandable RAM. The memory cells themselves can easily be copy-pasted vertically to expand the RAM.

``start`` and ``end`` variables represent the addresses values to start from and to stop to, they are BOTH included when creating the json file.

Take care not to create too big json files, since trying to import gigantic blueprints will make Factorio crash (talking from experience here).
Once you have acquired the json file, use the following command in a Linux terminal to convert it into a pastable Factorio blueprint :

``< [YOUR JSON FILE HERE] jq -c | zlib-flate -compress | base64 > [YOUR OUTFILE HERE]``

You might need to install some packages for that command to work, like ``zlib``, ``jq``, ``dpkg`` or ``qpdf``.

Now add the character ``0`` at the start of the string to make it valid.

And there you have your blueprint string, ready to be pasted in-game.
First build the amount of RAM cells you need, then paste this blueprint on top of the already built constant combinators to set them up properly.
