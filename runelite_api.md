MessageNode 	addChatMessage​(ChatMessageType type, String name, String message, String sender) 	
Adds a new chat message to the chatbox.

MessageNode 	addChatMessage​(ChatMessageType type, String name, String message, String sender, boolean postEvent) 	
Adds a new chat message to the chatbox.

void 	changeMemoryMode​(boolean lowMemory) 	
Changes how game behaves based on memory mode.

void 	changeWorld​(World world) 	
Changes the selected world to log in to.

void 	checkClickbox​(Projection projection, Model model, int orientation, int x, int y, int z, long hash) 	 

void 	clearHintArrow() 	\
Clears the current hint arrow.\

void 	closeInterface​(WidgetNode interfaceNode, boolean unload) 	\
Close an interface\

IndexedSprite 	createIndexedSprite() 	\
Creates an empty indexed sprite.\

SpritePixels 	createItemSprite​(int itemId, int quantity, int border, int shadowColor, int stackable, boolean noted, int scale) 	\
Creates an item icon sprite with passed variables.\

MenuEntry 	createMenuEntry​(int idx) 	\
Create a new menu entry\

default Projectile 	createProjectile​(int id, int plane, int startX, int startY, int startZ, int startCycle, int endCycle, int slope, int startHeight, int endHeight, Actor target, int targetX, int targetY) 	\
Deprecated.\

RuneLiteObject 	createRuneLiteObject() 	\
Creates a RuneLiteObject, which is a modified GraphicsObject\

ScriptEvent 	createScriptEvent​(Object... args) 	\
Creates a blank ScriptEvent for executing a ClientScript2 script\

SpritePixels 	createSpritePixels​(int[] pixels, int width, int height) 	\
Creates a sprite image with given width and height containing the pixels.\
World 	createWorld() 	\
Creates a new instance of a world.\

void 	draw2010Menu​(int alpha) 	\
Draws a menu in the 2010 interface style.\

SpritePixels 	drawInstanceMap​(int z) 	\
Draws an instance map for the current viewed plane.\

void 	drawOriginalMenu​(int alpha) 	\
Draws a menu in the OSRS interface style.\

Deprecated.
see Varbits#ACCOUNT_TYPE
Gets the ambient sound effects
NodeCache 	getAnimationCache() 	
Returns the client Animation cache
int[] 	getArray​(int arrayId) 	
Get one of the cs2 vm's arrays.
int 	getArraySizes​(int arrayId) 	
Get the size of one of the cs2 vm's arrays.
default int 	getBaseX() 	
Deprecated.
default int 	getBaseY() 	
Deprecated.
int 	getBoostedSkillLevel​(Skill skill) 	
Gets the current modified level of a skill.
int[] 	getBoostedSkillLevels() 	 
BufferProvider 	getBufferProvider() 	
Gets the clients graphic buffer provider.
String 	getBuildID() 	 
default NPC[] 	getCachedNPCs() 	
Deprecated.
default Player[] 	getCachedPlayers() 	
Deprecated.
Callbacks 	getCallbacks() 	
The injected client invokes these callbacks to send events to us
double 	getCameraFocalPointX() 	
Get the camera focus point x Typically this is the player position, but can be other points in cutscenes or in free camera mode.
double 	getCameraFocalPointY() 	
Get the camera focus point y Typically this is the player position, but can be other points in cutscenes or in free camera mode.
double 	getCameraFocalPointZ() 	
Get the camera focus point z Typically this is the player position, but can be other points in cutscenes or in free camera mode.
double 	getCameraFpPitch() 	
Floating point camera pitch.
double 	getCameraFpX() 	
Floating point camera position, x-axis
double 	getCameraFpY() 	
Floating point camera position, y-axis
double 	getCameraFpYaw() 	
Floating point camera yaw
double 	getCameraFpZ() 	
Floating point camera position, z-axis
int 	getCameraMode() 	
Get the camera mode
int 	getCameraPitch() 	
Gets the pitch of the camera.
int 	getCameraPitchTarget() 	
Get the target camera pitch The target pitch is the pitch the camera should use based on player input.
int 	getCameraX() 	
Gets the x-axis coordinate of the camera.
int 	getCameraY() 	
Gets the y-axis coordinate of the camera.
int 	getCameraYaw() 	
Gets the yaw of the camera.
int 	getCameraYawTarget() 	
Get the target camera yaw.
int 	getCameraZ() 	
Gets the z-axis coordinate of the camera.
Canvas 	getCanvas() 	
Gets the canvas that contains everything.
int 	getCanvasHeight() 	
Gets the canvas height
int 	getCanvasWidth() 	
Gets the canvas width
int 	getCenterX() 	 
int 	getCenterY() 	 
Map<Integer,​ChatLineBuffer> 	getChatLineMap() 	
Gets the map of chat buffers.
ClanChannel 	getClanChannel() 	
Get the primary clan channel the player is in.
ClanChannel 	getClanChannel​(int clanId) 	
Get clan channel by id.
ClanSettings 	getClanSettings() 	
Get clan settings for the clan the user is in.
ClanSettings 	getClanSettings​(int clanId) 	
Get clan settings by id
default CollisionData[] 	getCollisionMaps() 	
Deprecated.
HashTable<WidgetNode> 	getComponentTable() 	
Gets the widget node component table.
SpritePixels[] 	getCrossSprites() 	
Returns the array of cross sprites that appear and animate when left-clicking
long[] 	getCrossWorldMessageIds() 	
Get the list of message ids for the recently received cross-world messages.
int 	getCrossWorldMessageIdsIndex() 	
Get the index of the next message to be inserted in the cross world message id list
int 	getCurrentLoginField() 	
Gets currently selected login field.
DBRowConfig 	getDBRowConfig​(int rowID) 	 
List<Integer> 	getDBRowsByValue​(int table, int column, int tupleIndex, Object value) 	
Uses an index to find rows containing a certain value in a column.
Object[] 	getDBTableField​(int rowID, int column, int tupleIndex) 	
Gets a entry out of a DBTable Row
Widget 	getDraggedOnWidget() 	
Gets the widget that is being dragged on.
Widget 	getDraggedWidget() 	
Gets the widget currently being dragged.
int 	getDragTime() 	
Get the number of client cycles the current dragged widget has been dragged for.
DrawCallbacks 	getDrawCallbacks() 	
The injected client invokes these callbacks for scene drawing, which is used by the gpu plugin to override the client's normal scene drawing code
int 	getEnergy() 	
Gets the current run energy of the logged in player.
EnumComposition 	getEnum​(int id) 	 
int 	getExpandedMapLoading() 	 
NPC 	getFollower() 	
Get the local player's follower, such as a pet
int 	getFPS() 	
Gets the current FPS (frames per second).
FriendContainer 	getFriendContainer() 	
Retrieve the nameable container containing friends
FriendsChatManager 	getFriendsChatManager() 	
Retrieve the friends chat manager
int 	getGameCycle() 	
Gets the local clients game cycle.
GameState 	getGameState() 	
Gets the current game state.
GrandExchangeOffer[] 	getGrandExchangeOffers() 	
Gets an array of current grand exchange offers.
default Deque<GraphicsObject> 	getGraphicsObjects() 	
Deprecated.
ClanChannel 	getGuestClanChannel() 	
Get the guest clan channel the player is in.
ClanSettings 	getGuestClanSettings() 	
Get the guest clan's settings.
NPC 	getHintArrowNpc() 	
Gets the NPC that the hint arrow is directed at.
Player 	getHintArrowPlayer() 	
Gets the player that the hint arrow is directed at.
WorldPoint 	getHintArrowPoint() 	
Gets the world point that the hint arrow is directed at.
int 	getHintArrowType() 	
Gets the type of hint arrow currently displayed.
int 	getIdleTimeout() 	
Get the amount of time until the client automatically logs out due to idle input.
NameableContainer<Ignore> 	getIgnoreContainer() 	
Retrieve the nameable container containing ignores
IndexDataBase 	getIndex​(int id) 	
Gets an index by id
IndexDataBase 	getIndexConfig() 	
Gets the config index.
IndexDataBase 	getIndexScripts() 	
Gets the script index.
IndexDataBase 	getIndexSprites() 	
Gets the sprite index.
int[][][] 	getInstanceTemplateChunks() 	
Deprecated.
int[] 	getIntStack() 	
Gets the cs2 vm's int stack
int 	getIntStackSize() 	
Gets the length of the cs2 vm's int stack
NodeCache 	getItemCompositionCache() 	
Returns client item composition cache
ItemContainer 	getItemContainer​(int id) 	
Get an item container by id
ItemContainer 	getItemContainer​(InventoryID inventory) 	
Get the item container for an inventory.
HashTable<ItemContainer> 	getItemContainers() 	
Get all item containers
int 	getItemCount() 	
Returns the max item index + 1 from cache
ItemComposition 	getItemDefinition​(int id) 	
Gets the item composition corresponding to an items ID.
NodeCache 	getItemModelCache() 	
Get the item model cache.
NodeCache 	getItemSpriteCache() 	
Get the item sprite cache.
int 	getKeyboardIdleTicks() 	
Gets the amount of client ticks since the last keyboard press occurred.
String 	getLauncherDisplayName() 	
Gets the display name of the active account when launched from the Jagex launcher.
LocalPoint 	getLocalDestinationLocation() 	
Gets the location of the local player.
Player 	getLocalPlayer() 	
Gets the logged in player instance.
int 	getLoginIndex() 	
Gets index of current login state.
int 	getMapAngle() 	
Deprecated.
SpritePixels[] 	getMapDots() 	
Gets an array of currently drawn mini-map dots.
MapElementConfig 	getMapElementConfig​(int id) 	
Get a map element config by id
SpritePixels[] 	getMapIcons() 	
Gets an array of current map icon sprites.
int[] 	getMapRegions() 	
Deprecated.
IndexedSprite[] 	getMapScene() 	
Gets a sprite of the map scene
MenuEntry[] 	getMenuEntries() 	
Gets an array of currently open right-click menu entries that can be clicked and activated.
int 	getMenuHeight() 	
Get the menu height.
int 	getMenuScroll() 	
Get the number of entries the currently open menu has been scrolled down.
int 	getMenuWidth() 	
Get the menu width.
int 	getMenuX() 	
Get the menu x location.
int 	getMenuY() 	
Get the menu y location.
IterableHashTable<MessageNode> 	getMessages() 	
Map of message node id to message node
double 	getMinimapZoom() 	
Gets the number of pixels per tile on the minimap.
IndexedSprite[] 	getModIcons() 	
Gets an array of mod icon sprites.
Point 	getMouseCanvasPosition() 	
Gets the current position of the mouse on the canvas.
int 	getMouseCurrentButton() 	
Gets the current mouse button that is pressed.
int 	getMouseIdleTicks() 	
Gets the amount of client ticks since the last mouse movement occurred.
long 	getMouseLastPressedMillis() 	
Gets the time at which the last mouse press occurred in milliseconds since the UNIX epoch.
int 	getMusicVolume() 	
Gets the music volume
NPCComposition 	getNpcDefinition​(int npcId) 	
Gets the NPC composition corresponding to an NPCs ID.
default List<NPC> 	getNpcs() 	
Deprecated.
NodeCache 	getObjectCompositionCache() 	
Returns client object composition cache
ObjectComposition 	getObjectDefinition​(int objectId) 	
Gets the object composition corresponding to an objects ID.
int 	getOculusOrbFocalPointX() 	
Deprecated.
int 	getOculusOrbFocalPointY() 	
Deprecated.
int 	getOculusOrbState() 	
Deprecated.
long 	getOverallExperience() 	
Get the total experience of the player
default int 	getPlane() 	
Deprecated.
int[] 	getPlayerMenuTypes() 	
Gets an array of player menu types.
String[] 	getPlayerOptions() 	
Gets an array of options that can currently be used on other players.
boolean[] 	getPlayerOptionsPriorities() 	
Gets an array of whether an option is enabled or not.
default List<Player> 	getPlayers() 	
Deprecated.
Preferences 	getPreferences() 	
Gets the clients saved preferences.
default Deque<Projectile> 	getProjectiles() 	
Deprecated.
Rasterizer 	getRasterizer() 	 
int 	getRasterizer3D_clipMidX2() 	 
int 	getRasterizer3D_clipMidY2() 	 
int 	getRasterizer3D_clipNegativeMidX() 	 
int 	getRasterizer3D_clipNegativeMidY() 	 
Dimension 	getRealDimensions() 	
Gets the real dimensions of the client before being stretched.
int 	getRealSkillLevel​(Skill skill) 	
Gets the real level of a skill.
int[] 	getRealSkillLevels() 	 
RenderOverview 	getRenderOverview() 	
Deprecated.
int 	getRevision() 	
Gets the client revision number.
int 	getScale() 	
Gets the scale of the world (zoom value).
default Scene 	getScene() 	
Deprecated.
Widget 	getScriptActiveWidget() 	
Gets the cs2 vm's active widget This is used for all cc_* operations with a 0 operand
Widget 	getScriptDotWidget() 	
Gets the cs2 vm's "dot" widget This is used for all .cc_* operations with a 1 operand
default Tile 	getSelectedSceneTile() 	
Deprecated.
Widget 	getSelectedWidget() 	
Get the selected widget, such as a selected spell or selected item (eg.
int 	getServerVarbitValue​(int varbit) 	
Gets the value of the given varbit.
int[] 	getServerVarps() 	
Get an array of all server varplayers.
int 	getServerVarpValue​(int varpId) 	
Gets the value of a given VarPlayer.
int 	getSkillExperience​(Skill skill) 	
Gets the current experience towards a skill.
int[] 	getSkillExperiences() 	 
int 	getSkyboxColor() 	
Gets the RGB color of the skybox
Map<Integer,​SpritePixels> 	getSpriteOverrides() 	
Gets a mapping of sprites to override.
SpritePixels[] 	getSprites​(IndexDataBase source, int archiveId, int fileId) 	
Loads and creates the sprite images of the passed archive and file IDs.
Dimension 	getStretchedDimensions() 	
Gets the current stretched dimensions of the client.
String[] 	getStringStack() 	
Gets the cs2 vm's string stack
int 	getStringStackSize() 	
Gets the length of the cs2 vm's string stack
StructComposition 	getStructComposition​(int structID) 	
Gets the StructComposition for a given struct ID
NodeCache 	getStructCompositionCache() 	
Gets the client's cache of in memory struct compositions
TextureProvider 	getTextureProvider() 	 
int 	getTickCount() 	
Gets the current server tick count.
default int[][][] 	getTileHeights() 	
Deprecated.
default byte[][][] 	getTileSettings() 	
Deprecated.
int 	getTopLevelInterfaceId() 	
Gets Interface ID of the root widget
WorldView 	getTopLevelWorldView() 	
Get the top level world view
int 	getTotalLevel() 	
Calculates the total level from real skill levels.
String 	getUsername() 	
Deprecated.
int 	getVar​(int varbit) 	
Deprecated.
VarbitComposition 	getVarbit​(int id) 	
Gets the varbit composition for a given varbit id
int 	getVarbitValue​(int varbit) 	
Gets the value of the given varbit.
int 	getVarbitValue​(int[] varps, int varbitId) 	
Gets the value of a given variable.
int 	getVarcIntValue​(int var) 	
Gets the value of a given VarClientInt
Map<Integer,​Object> 	getVarcMap() 	
Gets an array of all client variables.
String 	getVarcStrValue​(int var) 	
Gets the value of a given VarClientStr
int[] 	getVarps() 	
Gets an array of all client varplayers.
int 	getVarpValue​(int varpId) 	
Gets the value of a given VarPlayer.
int 	getViewportHeight() 	
Gets the height of the viewport.
int 	getViewportWidth() 	
Gets the width of the viewport.
int 	getViewportXOffset() 	
Gets the x-axis offset of the viewport.
int 	getViewportYOffset() 	
Gets the y-axis offset of the viewport.
int 	getWeight() 	
Gets the current weight of the logged in player.
Widget 	getWidget​(int componentId) 	
Gets a widget by its component id.
Widget 	getWidget​(int groupId, int childId) 	
Gets a widget by its raw group ID and child ID.
Widget 	getWidget​(WidgetInfo widget) 	
Deprecated.
HashTable<IntegerNode> 	getWidgetFlags() 	
Gets the widget flags table.
int[] 	getWidgetPositionsX() 	
Gets an array containing the x-axis canvas positions of all widgets.
int[] 	getWidgetPositionsY() 	
Gets an array containing the y-axis canvas positions of all widgets.
Widget[] 	getWidgetRoots() 	
Gets the root widgets.
NodeCache 	getWidgetSpriteCache() 	
Returns widget sprite cache, to be used with getSpriteOverrides()
Map<Integer,​SpritePixels> 	getWidgetSpriteOverrides() 	
Gets a mapping of widget sprites to override.
int 	getWorld() 	
Gets the current world number of the logged in player.
World[] 	getWorldList() 	
Gets a list of all RuneScape worlds.
WorldMap 	getWorldMap() 	
Get the world map
EnumSet<WorldType> 	getWorldType() 	
Gets a set of current world types that apply to the logged in world.
WorldView 	getWorldView​(int id) 	
Get worldview by id
int[][] 	getXteaKeys() 	
Deprecated.
boolean 	hasHintArrow() 	
Checks whether or not there is any active hint arrow.
void 	hopToWorld​(World world) 	
Hops using in-game world hopper widget to another world
void 	invalidateStretching​(boolean resize) 	
Invalidates cached dimensions that are used for stretching and scaling.
boolean 	isDraggingWidget() 	
Checks whether a widget is currently being dragged.
boolean 	isFriended​(String name, boolean mustBeLoggedIn) 	
Checks whether a player is on the friends list.
boolean 	isGpu() 	 
boolean 	isInInstancedRegion() 	
Deprecated.
boolean 	isInterpolateNpcAnimations() 	
Checks whether animation smoothing is enabled for NPC.
boolean 	isInterpolateObjectAnimations() 	
Checks whether animation smoothing is enabled for objects.
boolean 	isInterpolatePlayerAnimations() 	
Checks whether animation smoothing is enabled for players.
boolean 	isKeyPressed​(int keycode) 	
Test if a key is pressed
boolean 	isMenuOpen() 	
Checks whether a right-click menu is currently open.
boolean 	isMenuScrollable() 	
Returns whether the currently open menu is scrollable.
boolean 	isMinimapZoom() 	
Get whether minimap zoom is enabled
boolean 	isPrayerActive​(Prayer prayer) 	
Checks whether or not a prayer is currently active.
boolean 	isResized() 	
Checks whether the client window is currently resized.
boolean 	isStretchedEnabled() 	
Checks whether the client is in stretched mode.
boolean 	isStretchedFast() 	
Checks whether the client is using fast rendering techniques when stretching the canvas.
boolean 	isWidgetSelected() 	
Is a widget is in target mode?
Animation 	loadAnimation​(int id) 	
Loads an animation from the cache
Model 	loadModel​(int id) 	
Loads and lights a model from the cache This is equivalent to loadModelData(id).light()
Model 	loadModel​(int id, short[] colorToFind, short[] colorToReplace) 	
Loads a model from the cache and also recolors it
ModelData 	loadModelData​(int id) 	
Loads an unlit model from the cache.
void 	menuAction​(int p0, int p1, MenuAction action, int id, int itemId, String option, String target) 	 
ModelData 	mergeModels​(ModelData... models) 	 
ModelData 	mergeModels​(ModelData[] models, int length) 	 
WidgetNode 	openInterface​(int componentId, int interfaceId, int modalMode) 	
Open an interface.
void 	openWorldHopper() 	
Opens in-game world hopper interface
void 	playSoundEffect​(int id) 	
Play a sound effect at the player's current location.
void 	playSoundEffect​(int id, int volume) 	
Plays a sound effect, even if the player's sound effect volume is muted.
void 	playSoundEffect​(int id, int x, int y, int range) 	
Play a sound effect from some point in the world.
void 	playSoundEffect​(int id, int x, int y, int range, int delay) 	
Play a sound effect from some point in the world.
void 	queueChangedSkill​(Skill skill) 	 
void 	queueChangedVarp​(int varp) 	
Mark the given varp as changed, causing var listeners to be triggered next tick
void 	refreshChat() 	
Refreshes the chat.
void 	resetHealthBarCaches() 	 
void 	runScript​(Object... args) 	
Executes a client script from the cache This method must be ran on the client thread and is not reentrant This method is shorthand for client.createScriptEvent(args).run()
void 	setAllWidgetsAreOpTargetable​(boolean value) 	
Makes all widgets behave as if they are WidgetConfig.WIDGET_USE_TARGET
void 	setCameraFocalPointX​(double x) 	
Sets the camera focus point x.
void 	setCameraFocalPointY​(double y) 	
Sets the camera focus point y.
void 	setCameraFocalPointZ​(double z) 	
Sets the camera focus point z.
void 	setCameraMode​(int mode) 	
Set the camera mode
void 	setCameraMouseButtonMask​(int mask) 	
Sets the mask for which mouse buttons control the camera.
void 	setCameraPitchRelaxerEnabled​(boolean enabled) 	
Sets whether the camera pitch can exceed the normal limits set by the RuneScape client.
void 	setCameraPitchTarget​(int cameraPitchTarget) 	
Set the target camera pitch
void 	setCameraSpeed​(float speed) 	
Sets the camera speed
void 	setCameraYawTarget​(int cameraYawTarget) 	
Set the target camera yaw
void 	setCompass​(SpritePixels spritePixels) 	
Sets the compass sprite.
void 	setDraggedOnWidget​(Widget widget) 	
Sets the widget that is being dragged on.
void 	setDrawCallbacks​(DrawCallbacks drawCallbacks) 	 
void 	setExpandedMapLoading​(int chunks) 	 
void 	setFreeCameraSpeed​(int speed) 	
Sets the normal moving speed when using oculus orb (default value is 12)
void 	setGameState​(GameState gameState) 	
Sets the current game state
void 	setGeSearchResultCount​(int count) 	
Sets the result count for GE search
void 	setGeSearchResultIds​(short[] ids) 	
Sets the array of item ids for GE search
void 	setGeSearchResultIndex​(int index) 	
Sets the starting index in the item id array for GE search
void 	setGpuFlags​(int gpuflags) 	 
void 	setHintArrow​(LocalPoint point) 	
Sets the hint arrow to the passsed point
void 	setHintArrow​(WorldPoint point) 	
Sets a hint arrow to point to the passed location.
void 	setHintArrow​(NPC npc) 	
Sets a hint arrow to point to the passed NPC.
void 	setHintArrow​(Player player) 	
Sets a hint arrow to point to the passed player.
void 	setIdleTimeout​(int ticks) 	
Set the amount of time until the client automatically logs out due to idle input.
void 	setInterpolateNpcAnimations​(boolean interpolate) 	
Sets the animation smoothing state for NPCs.
void 	setInterpolateObjectAnimations​(boolean interpolate) 	
Sets the animation smoothing state for objects.
void 	setInterpolatePlayerAnimations​(boolean interpolate) 	
Sets the animation smoothing state for players.
void 	setIntStackSize​(int stackSize) 	
Sets the length of the cs2 vm's int stack
void 	setInventoryDragDelay​(int delay) 	
Deprecated.
void 	setInvertPitch​(boolean invertPitch) 	
Sets if the moving the camera vertically should be backwards
void 	setInvertYaw​(boolean invertYaw) 	
Sets if the moving the camera horizontally should be backwards
void 	setLoginScreen​(SpritePixels pixels) 	
Sets the image to be used for the login screen, provided as SpritePixels If the image is larger than half the width of fixed mode, it won't get mirrored to the other side of the screen
void 	setMenuEntries​(MenuEntry[] entries) 	
Sets the array of open menu entries.
void 	setMenuScroll​(int scroll) 	
Set the number of entries the currently open menu has been scrolled down.
void 	setMinimapTileDrawer​(TileFunction drawTile) 	
Sets a callback to override the drawing of tiles on the minimap.
void 	setMinimapZoom​(boolean minimapZoom) 	
Set whether minimap zoom is enabled
void 	setMinimapZoom​(double zoom) 	
Set the number of pixels per tile on the minimap.
void 	setModIcons​(IndexedSprite[] modIcons) 	
Replaces the current mod icons with a new array.
void 	setMusicVolume​(int volume) 	
Sets the music volume
void 	setOculusOrbNormalSpeed​(int speed) 	
Deprecated.
void 	setOculusOrbState​(int state) 	
Deprecated.
void 	setOtp​(String otp) 	
Sets the 6 digit pin used for authenticator on login screen.
void 	setPassword​(String password) 	
Sets the password on login screen.
void 	setScalingFactor​(int factor) 	
Sets the scaling factor when scaling resizable mode.
void 	setShouldRenderLoginScreenFire​(boolean val) 	
Sets whether the flames on the login screen should be rendered
void 	setSkyboxColor​(int skyboxColor) 	
Sets the RGB color of the skybox
void 	setStretchedEnabled​(boolean state) 	
Sets the client stretched mode state.
void 	setStretchedFast​(boolean state) 	
Sets whether to use fast rendering techniques when stretching the canvas.
void 	setStretchedIntegerScaling​(boolean state) 	
Sets whether to force integer scale factor by rounding scale factors towards zero when stretching.
void 	setStretchedKeepAspectRatio​(boolean state) 	
Sets whether to keep aspect ratio when stretching.
void 	setStringStackSize​(int stackSize) 	
Sets the length of the cs2 vm's string stack
void 	setTickCount​(int tickCount) 	
Sets the current server tick count.
void 	setUnlockedFps​(boolean unlock) 	 
void 	setUnlockedFpsTarget​(int fps) 	 
void 	setUsername​(String name) 	
Sets the current logged in username.
void 	setVarbit​(int varbit, int value) 	
Sets the value of a varbit
void 	setVarbitValue​(int[] varps, int varbit, int value) 	
Sets the value of a given variable.
void 	setVarcIntValue​(int var, int value) 	
Sets a VarClientInt to the passed value
void 	setVarcStrValue​(int var, String value) 	
Sets a VarClientString to the passed value
void 	setWidgetSelected​(boolean selected) 	
Sets if a widget is in target mode
void 	stopNow() 	
Causes the client to shutdown.
    Methods inherited from interface net.runelite.api.GameEngine
    getClientThread, isClientThread, resizeCanvas
    Methods inherited from interface com.jagex.oldscape.pub.OAuthApi
    getAccountHash

Method Detail
    getCallbacks

    Callbacks getCallbacks()

    The injected client invokes these callbacks to send events to us
    getDrawCallbacks

    DrawCallbacks getDrawCallbacks()

    The injected client invokes these callbacks for scene drawing, which is used by the gpu plugin to override the client's normal scene drawing code
    setDrawCallbacks

    void setDrawCallbacks​(DrawCallbacks drawCallbacks)

    getBuildID

    String getBuildID()

    getBoostedSkillLevel

    int getBoostedSkillLevel​(Skill skill)

    Gets the current modified level of a skill.

    Parameters:
        skill - the skill
    Returns:
        the modified skill level

    getRealSkillLevel

    int getRealSkillLevel​(Skill skill)

    Gets the real level of a skill.

    Parameters:
        skill - the skill
    Returns:
        the skill level

    getTotalLevel

    int getTotalLevel()

    Calculates the total level from real skill levels.

    Returns:
        the total level

    addChatMessage

    MessageNode addChatMessage​(ChatMessageType type, String name, String message, String sender)

    Adds a new chat message to the chatbox.

    Parameters:
        type - the type of message
        name - the name of the player that sent the message
        message - the message contents
        sender - the sender/channel name
    Returns:
        the message node for the message

    addChatMessage

    MessageNode addChatMessage​(ChatMessageType type, String name, String message, String sender, boolean postEvent)

    Adds a new chat message to the chatbox.

    Parameters:
        type - the type of message
        name - the name of the player that sent the message
        message - the message contents
        sender - the sender/channel name
        postEvent - whether to post the chat message event
    Returns:
        the message node for the message

    getGameState

    GameState getGameState()

    Gets the current game state.

    Returns:
        the game state

    setGameState

    void setGameState​(GameState gameState)

    Sets the current game state

    Parameters:
        gameState - 

    stopNow

    void stopNow()

    Causes the client to shutdown. It is faster than Applet.stop() because it doesn't wait for 4000ms. This will call System.exit(int) when it is done
    getLauncherDisplayName

    @Nullable String getLauncherDisplayName()

    Gets the display name of the active account when launched from the Jagex launcher.

    Returns:
        The active account's display name, or null if not launched from the Jagex launcher

    getUsername

    @Deprecated String getUsername()

    Deprecated.
    DEPRECATED. See getAccountHash instead. Gets the current logged in username.

    Returns:
        the logged in username
    See Also:
        OAuthApi.getAccountHash()

    setUsername

    void setUsername​(String name)

    Sets the current logged in username.

    Parameters:
        name - the logged in username

    setPassword

    void setPassword​(String password)

    Sets the password on login screen.

    Parameters:
        password - the login screen password

    setOtp

    void setOtp​(String otp)

    Sets the 6 digit pin used for authenticator on login screen.

    Parameters:
        otp - one time password

    getCurrentLoginField

    int getCurrentLoginField()

    Gets currently selected login field. 0 is username, and 1 is password.

    Returns:
        currently selected login field

    getLoginIndex

    int getLoginIndex()

    Gets index of current login state. 2 is username/password form, 4 is authenticator form

    Returns:
        current login state index

    getAccountType

    @Deprecated AccountType getAccountType()

    Deprecated. see Varbits#ACCOUNT_TYPE Gets the account type of the logged in player.

    Returns:
        the account type

    getCanvas

    Canvas getCanvas()

    Description copied from interface: GameEngine
    Gets the canvas that contains everything.

    Specified by:
        getCanvas in interface GameEngine
    Returns:
        the game canvas

    getFPS

    int getFPS()

    Gets the current FPS (frames per second).

    Returns:
        the FPS

    getCameraX

    int getCameraX()

    Gets the x-axis coordinate of the camera.

    This value is a local coordinate value similar to getLocalDestinationLocation().

    Returns:
        the camera x coordinate

    getCameraFpX

    double getCameraFpX()

    Floating point camera position, x-axis

    Returns:
    See Also:
        getCameraX()

    getCameraY

    int getCameraY()

    Gets the y-axis coordinate of the camera.

    This value is a local coordinate value similar to getLocalDestinationLocation().

    Returns:
        the camera y coordinate

    getCameraFpY

    double getCameraFpY()

    Floating point camera position, y-axis

    Returns:
    See Also:
        getCameraY()

    getCameraZ

    int getCameraZ()

    Gets the z-axis coordinate of the camera.

    This value is a local coordinate value similar to getLocalDestinationLocation().

    Returns:
        the camera z coordinate

    getCameraFpZ

    double getCameraFpZ()

    Floating point camera position, z-axis

    Returns:
    See Also:
        getCameraZ()

    getCameraPitch

    int getCameraPitch()

    Gets the pitch of the camera.

    The value returned by this method is measured in JAU, or Jagex Angle Unit, which is 1/1024 of a revolution.

    Returns:
        the camera pitch

    getCameraFpPitch

    double getCameraFpPitch()

    Floating point camera pitch.

    Returns:
    See Also:
        getCameraPitch()

    getCameraYaw

    int getCameraYaw()

    Gets the yaw of the camera.

    Returns:
        the camera yaw

    getCameraFpYaw

    double getCameraFpYaw()

    Floating point camera yaw

    Returns:
    See Also:
        getCameraYaw()

    getWorld

    int getWorld()

    Gets the current world number of the logged in player.

    Returns:
        the logged in world number

    getCanvasHeight

    int getCanvasHeight()

    Gets the canvas height

    Returns:

    getCanvasWidth

    int getCanvasWidth()

    Gets the canvas width

    Returns:

    getViewportHeight

    int getViewportHeight()

    Gets the height of the viewport.

    Returns:
        the viewport height

    getViewportWidth

    int getViewportWidth()

    Gets the width of the viewport.

    Returns:
        the viewport width

    getViewportXOffset

    int getViewportXOffset()

    Gets the x-axis offset of the viewport.

    Returns:
        the x-axis offset

    getViewportYOffset

    int getViewportYOffset()

    Gets the y-axis offset of the viewport.

    Returns:
        the y-axis offset

    getScale

    int getScale()

    Gets the scale of the world (zoom value).

    Returns:
        the world scale

    getMouseCanvasPosition

    Point getMouseCanvasPosition()

    Gets the current position of the mouse on the canvas.

    Returns:
        the mouse canvas position

    getLocalPlayer

    Player getLocalPlayer()

    Gets the logged in player instance.

    Returns:
        the logged in player

    getFollower

    @Nullable NPC getFollower()

    Get the local player's follower, such as a pet

    Returns:

    getItemDefinition

    @Nonnull ItemComposition getItemDefinition​(int id)

    Gets the item composition corresponding to an items ID.

    Parameters:
        id - the item ID
    Returns:
        the corresponding item composition
    See Also:
        ItemID

    createItemSprite

    @Nullable SpritePixels createItemSprite​(int itemId, int quantity, int border, int shadowColor, int stackable, boolean noted, int scale)

    Creates an item icon sprite with passed variables.

    Parameters:
        itemId - the item ID
        quantity - the item quantity
        border - whether to draw a border
        shadowColor - the shadow color
        stackable - whether the item is stackable
        noted - whether the item is noted
        scale - the scale of the sprite
    Returns:
        the created sprite

    getItemModelCache

    NodeCache getItemModelCache()

    Get the item model cache. These models are used for drawing widgets of type WidgetType.MODEL and inventory item icons

    Returns:

    getItemSpriteCache

    NodeCache getItemSpriteCache()

    Get the item sprite cache. These are 2d SpritePixels which are used to raster item images on the inventory and on widgets of type WidgetType.GRAPHIC

    Returns:

    getSprites

    @Nullable SpritePixels[] getSprites​(IndexDataBase source, int archiveId, int fileId)

    Loads and creates the sprite images of the passed archive and file IDs.

    Parameters:
        source - the sprite index
        archiveId - the sprites archive ID
        fileId - the sprites file ID
    Returns:
        the sprite image of the file

    getIndexSprites

    IndexDataBase getIndexSprites()

    Gets the sprite index.
    getIndexScripts

    IndexDataBase getIndexScripts()

    Gets the script index.
    getIndexConfig

    IndexDataBase getIndexConfig()

    Gets the config index.
    getIndex

    IndexDataBase getIndex​(int id)

    Gets an index by id
    getMouseCurrentButton

    int getMouseCurrentButton()

    Gets the current mouse button that is pressed.

    Returns:
        the pressed mouse button

    isDraggingWidget

    boolean isDraggingWidget()

    Checks whether a widget is currently being dragged.

    Returns:
        true if dragging a widget, false otherwise

    getDraggedWidget

    @Nullable Widget getDraggedWidget()

    Gets the widget currently being dragged.

    Returns:
        the dragged widget, null if not dragging any widget

    getDraggedOnWidget

    @Nullable Widget getDraggedOnWidget()

    Gets the widget that is being dragged on.

    The widget being dragged has the WidgetConfig.DRAG flag set, and is the widget currently under the dragged widget.

    Returns:
        the dragged on widget, null if not dragging any widget

    setDraggedOnWidget

    void setDraggedOnWidget​(Widget widget)

    Sets the widget that is being dragged on.

    Parameters:
        widget - the new dragged on widget

    getDragTime

    int getDragTime()

    Get the number of client cycles the current dragged widget has been dragged for.

    Returns:

    getTopLevelInterfaceId

    @Interface int getTopLevelInterfaceId()

    Gets Interface ID of the root widget
    getWidgetRoots

    Widget[] getWidgetRoots()

    Gets the root widgets.

    Returns:
        the root widgets

    getWidget

    @Nullable @Deprecated Widget getWidget​(WidgetInfo widget)

    Deprecated.
    Gets a widget corresponding to the passed widget info.

    Parameters:
        widget - the widget info
    Returns:
        the widget

    getWidget

    @Nullable Widget getWidget​(@Interface int groupId, int childId)

    Gets a widget by its raw group ID and child ID.

    Parameters:
        groupId - the group ID
        childId - the child widget ID
    Returns:
        the widget corresponding to the group and child pair

    getWidget

    @Nullable Widget getWidget​(@Component int componentId)

    Gets a widget by its component id.

    Parameters:
        componentId - the component id

    getWidgetPositionsX

    int[] getWidgetPositionsX()

    Gets an array containing the x-axis canvas positions of all widgets.

    Returns:
        array of x-axis widget coordinates

    getWidgetPositionsY

    int[] getWidgetPositionsY()

    Gets an array containing the y-axis canvas positions of all widgets.

    Returns:
        array of y-axis widget coordinates

    getEnergy

    int getEnergy()

    Gets the current run energy of the logged in player.

    Returns:
        the run energy in units of 1/100th of an percentage

    getWeight

    int getWeight()

    Gets the current weight of the logged in player.

    Returns:
        the weight

    getPlayerOptions

    String[] getPlayerOptions()

    Gets an array of options that can currently be used on other players.

    For example, if the player is in a PVP area the "Attack" option will become available in the array. Otherwise, it won't be there.

    Returns:
        an array of options

    getPlayerOptionsPriorities

    boolean[] getPlayerOptionsPriorities()

    Gets an array of whether an option is enabled or not.

    Returns:
        the option priorities

    getPlayerMenuTypes

    int[] getPlayerMenuTypes()

    Gets an array of player menu types.

    Returns:
        the player menu types

    getWorldList

    World[] getWorldList()

    Gets a list of all RuneScape worlds.

    Returns:
        world list

    createMenuEntry

    MenuEntry createMenuEntry​(int idx)

    Create a new menu entry

    Parameters:
        idx - the index to create the menu entry at. Accepts negative indexes eg. -1 inserts at the end.
    Returns:
        the newly created menu entry

    getMenuEntries

    MenuEntry[] getMenuEntries()

    Gets an array of currently open right-click menu entries that can be clicked and activated.

    Returns:
        array of open menu entries

    setMenuEntries

    void setMenuEntries​(MenuEntry[] entries)

    Sets the array of open menu entries.

    This method should typically be used in the context of the MenuOpened event, since setting the menu entries will be overwritten the next frame

    Parameters:
        entries - new array of open menu entries

    isMenuOpen

    boolean isMenuOpen()

    Checks whether a right-click menu is currently open.

    Returns:
        true if a menu is open, false otherwise

    isMenuScrollable

    boolean isMenuScrollable()

    Returns whether the currently open menu is scrollable.

    Returns:

    getMenuScroll

    int getMenuScroll()

    Get the number of entries the currently open menu has been scrolled down.

    Returns:

    setMenuScroll

    void setMenuScroll​(int scroll)

    Set the number of entries the currently open menu has been scrolled down.

    Parameters:
        scroll - 

    getMenuX

    int getMenuX()

    Get the menu x location. Only valid if the menu is open.

    Returns:
        the menu x location

    getMenuY

    int getMenuY()

    Get the menu y location. Only valid if the menu is open.

    Returns:
        the menu y location

    getMenuHeight

    int getMenuHeight()

    Get the menu height. Only valid if the menu is open.

    Returns:
        the menu height

    getMenuWidth

    int getMenuWidth()

    Get the menu width. Only valid if the menu is open.

    Returns:
        the menu width

    getMapAngle

    @Deprecated int getMapAngle()

    Deprecated.
    Gets the angle of the map, or target camera yaw.

    Returns:
        the map angle
    See Also:
        getCameraYawTarget()

    isResized

    boolean isResized()

    Checks whether the client window is currently resized.

    Returns:
        true if resized, false otherwise

    getRevision

    int getRevision()

    Gets the client revision number.

    Returns:
        the revision

    getVarps

    @VisibleForDevtools int[] getVarps()

    Gets an array of all client varplayers.

    Returns:
        local player variables

    getServerVarps

    @VisibleForDevtools int[] getServerVarps()

    Get an array of all server varplayers. These vars are only modified by the server, and so represent the server's idea of the varp values.

    Returns:
        the server varps

    getVarcMap

    @VisibleForDevtools Map<Integer,​Object> getVarcMap()

    Gets an array of all client variables.
    getVar

    @Deprecated int getVar​(@Varbit int varbit)

    Deprecated.
    Gets a value corresponding to the passed varbit.

    Parameters:
        varbit - the varbit id
    Returns:
        the value
    See Also:
        getVarbitValue(int)

    getVarbitValue

    int getVarbitValue​(@Varbit int varbit)

    Gets the value of the given varbit.

    Parameters:
        varbit - the varbit id
    Returns:
        the value

    getServerVarbitValue

    int getServerVarbitValue​(@Varbit int varbit)

    Gets the value of the given varbit. This returns the server's idea of the value, not the client's. This is specifically the last value set by the server regardless of changes to the var by the client.

    Parameters:
        varbit - the varbit id
    Returns:
        the value

    getVarpValue

    int getVarpValue​(@Varp int varpId)

    Gets the value of a given VarPlayer.

    Parameters:
        varpId - the VarPlayer id
    Returns:
        the value

    getServerVarpValue

    int getServerVarpValue​(@Varp int varpId)

    Gets the value of a given VarPlayer. This returns the server's idea of the value, not the client's. This is specifically the last value set by the server regardless of changes to the var by the client.

    Parameters:
        varpId - the VarPlayer id
    Returns:
        the value

    getVarcIntValue

    int getVarcIntValue​(@VarCInt int var)

    Gets the value of a given VarClientInt

    Parameters:
        var - the VarClientInt
    Returns:
        the value

    getVarcStrValue

    String getVarcStrValue​(@VarCStr int var)

    Gets the value of a given VarClientStr

    Parameters:
        var - the VarClientStr
    Returns:
        the value

    setVarcStrValue

    void setVarcStrValue​(@VarCStr int var, String value)

    Sets a VarClientString to the passed value

    Parameters:
        var - the VarClientStr
        value - the new value

    setVarcIntValue

    void setVarcIntValue​(@VarCInt int var, int value)

    Sets a VarClientInt to the passed value

    Parameters:
        var - the VarClientInt
        value - the new value

    setVarbit

    void setVarbit​(@Varbit int varbit, int value)

    Sets the value of a varbit

    Parameters:
        varbit - the varbit id
        value - the new value

    getVarbit

    @VisibleForDevtools @Nullable VarbitComposition getVarbit​(int id)

    Gets the varbit composition for a given varbit id

    Parameters:
        id - 
    Returns:

    getVarbitValue

    @VisibleForDevtools int getVarbitValue​(int[] varps, @Varbit int varbitId)

    Gets the value of a given variable.

    Parameters:
        varps - passed varbits
        varbitId - the variable ID
    Returns:
        the value
    See Also:
        Varbits

    setVarbitValue

    @VisibleForDevtools void setVarbitValue​(int[] varps, @Varbit int varbit, int value)

    Sets the value of a given variable.

    Parameters:
        varps - passed varbits
        varbit - the variable
        value - the value
    See Also:
        Varbits

    queueChangedVarp

    void queueChangedVarp​(@Varp int varp)

    Mark the given varp as changed, causing var listeners to be triggered next tick

    Parameters:
        varp - 

    openInterface

    WidgetNode openInterface​(int componentId, int interfaceId, int modalMode)

    Open an interface.

    Parameters:
        componentId - component id to open the interface at
        interfaceId - the interface to open
        modalMode - see WidgetModalMode
    Returns:
        the WidgetNode for the interface. This should be closed later by calling {closeInterface(WidgetNode, boolean).
    Throws:
        IllegalStateException - if the component does not exist or it not a layer, or the interface is already open on a different component

    closeInterface

    void closeInterface​(WidgetNode interfaceNode, boolean unload)

    Close an interface

    Parameters:
        interfaceNode - the WidgetNode linking the interface into the component tree
        unload - whether to null the client's widget table
    Throws:
        IllegalArgumentException - if the interfaceNode is not linked into the component tree

    getWidgetFlags

    HashTable<IntegerNode> getWidgetFlags()

    Gets the widget flags table.

    Returns:
        the widget flags table

    getComponentTable

    HashTable<WidgetNode> getComponentTable()

    Gets the widget node component table.

    Returns:
        the widget node component table
    See Also:
        WidgetNode

    getGrandExchangeOffers

    GrandExchangeOffer[] getGrandExchangeOffers()

    Gets an array of current grand exchange offers.

    Returns:
        all grand exchange offers

    isPrayerActive

    boolean isPrayerActive​(Prayer prayer)

    Checks whether or not a prayer is currently active.

    Parameters:
        prayer - the prayer
    Returns:
        true if the prayer is active, false otherwise

    getSkillExperience

    int getSkillExperience​(Skill skill)

    Gets the current experience towards a skill.

    Parameters:
        skill - the skill
    Returns:
        the experience

    getOverallExperience

    long getOverallExperience()

    Get the total experience of the player

    Returns:

    refreshChat

    void refreshChat()

    Refreshes the chat.
    getChatLineMap

    Map<Integer,​ChatLineBuffer> getChatLineMap()

    Gets the map of chat buffers.

    Returns:
        the chat buffers

    getMessages

    IterableHashTable<MessageNode> getMessages()

    Map of message node id to message node

    Returns:
        the map

    getObjectDefinition

    ObjectComposition getObjectDefinition​(int objectId)

    Gets the object composition corresponding to an objects ID.

    Parameters:
        objectId - the object ID
    Returns:
        the corresponding object composition
    See Also:
        ObjectID

    getNpcDefinition

    NPCComposition getNpcDefinition​(int npcId)

    Gets the NPC composition corresponding to an NPCs ID.

    Parameters:
        npcId - the npc ID
    Returns:
        the corresponding NPC composition
    See Also:
        NpcID

    getStructComposition

    StructComposition getStructComposition​(int structID)

    Gets the StructComposition for a given struct ID

    See Also:
        StructID

    getStructCompositionCache

    NodeCache getStructCompositionCache()

    Gets the client's cache of in memory struct compositions
    getDBTableField

    Object[] getDBTableField​(int rowID, int column, int tupleIndex)

    Gets a entry out of a DBTable Row
    getDBRowConfig

    DBRowConfig getDBRowConfig​(int rowID)

    getDBRowsByValue

    List<Integer> getDBRowsByValue​(int table, int column, int tupleIndex, Object value)

    Uses an index to find rows containing a certain value in a column. An index must exist for this column.
    getMapElementConfig

    MapElementConfig getMapElementConfig​(int id)

    Get a map element config by id

    Parameters:
        id - the id

    getMapScene

    IndexedSprite[] getMapScene()

    Gets a sprite of the map scene

    Returns:
        the sprite

    getMapDots

    SpritePixels[] getMapDots()

    Gets an array of currently drawn mini-map dots.

    Returns:
        all mini-map dots

    getGameCycle

    int getGameCycle()

    Gets the local clients game cycle.

    Note: This value is incremented every 20ms.

    Returns:
        the game cycle

    getMapIcons

    SpritePixels[] getMapIcons()

    Gets an array of current map icon sprites.

    Returns:
        the map icons

    getModIcons

    IndexedSprite[] getModIcons()

    Gets an array of mod icon sprites.

    Returns:
        the mod icons

    setModIcons

    void setModIcons​(IndexedSprite[] modIcons)

    Replaces the current mod icons with a new array.

    Parameters:
        modIcons - the new mod icons

    createIndexedSprite

    IndexedSprite createIndexedSprite()

    Creates an empty indexed sprite.

    Returns:
        the sprite

    createSpritePixels

    SpritePixels createSpritePixels​(int[] pixels, int width, int height)

    Creates a sprite image with given width and height containing the pixels.

    Parameters:
        pixels - the pixels
        width - the width
        height - the height
    Returns:
        the sprite image

    getLocalDestinationLocation

    @Nullable LocalPoint getLocalDestinationLocation()

    Gets the location of the local player.

    Returns:
        the local player location

    createRuneLiteObject

    RuneLiteObject createRuneLiteObject()

    Creates a RuneLiteObject, which is a modified GraphicsObject
    loadModelData

    @Nullable ModelData loadModelData​(int id)

    Loads an unlit model from the cache. The returned model shares data such as faces, face colors, face transparencies, and vertex points with other models. If you want to mutate these you MUST call the relevant cloneX method.

    Parameters:
        id - the ID of the model
    Returns:
        the model or null if it is loading or nonexistent
    See Also:
        ModelData.cloneColors()

    mergeModels

    ModelData mergeModels​(ModelData[] models, int length)

    mergeModels

    ModelData mergeModels​(ModelData... models)

    loadModel

    @Nullable Model loadModel​(int id)

    Loads and lights a model from the cache This is equivalent to loadModelData(id).light()

    Parameters:
        id - the ID of the model
    Returns:
        the model or null if it is loading or nonexistent

    loadModel

    @Nullable Model loadModel​(int id, short[] colorToFind, short[] colorToReplace)

    Loads a model from the cache and also recolors it

    Parameters:
        id - the ID of the model
        colorToFind - array of hsl color values to find in the model to replace
        colorToReplace - array of hsl color values to replace in the model
    Returns:
        the model or null if it is loading or nonexistent

    loadAnimation

    Animation loadAnimation​(int id)

    Loads an animation from the cache

    Parameters:
        id - the ID of the animation. Any int is allowed, but implementations in the client should be defined in AnimationID

    getMusicVolume

    int getMusicVolume()

    Gets the music volume

    Returns:
        volume 0-255 inclusive

    setMusicVolume

    void setMusicVolume​(int volume)

    Sets the music volume

    Parameters:
        volume - 0-255 inclusive

    playSoundEffect

    void playSoundEffect​(int id)

    Play a sound effect at the player's current location. This is how UI, and player-generated (e.g. mining, woodcutting) sound effects are normally played.

    Parameters:
        id - the ID of the sound to play. Any int is allowed, but see SoundEffectID for some common ones

    playSoundEffect

    void playSoundEffect​(int id, int x, int y, int range)

    Play a sound effect from some point in the world.

    Parameters:
        id - the ID of the sound to play. Any int is allowed, but see SoundEffectID for some common ones
        x - the ground coordinate on the x axis
        y - the ground coordinate on the y axis
        range - the number of tiles away that the sound can be heard from

    playSoundEffect

    void playSoundEffect​(int id, int x, int y, int range, int delay)

    Play a sound effect from some point in the world.

    Parameters:
        id - the ID of the sound to play. Any int is allowed, but see SoundEffectID for some common ones
        x - the ground coordinate on the x axis
        y - the ground coordinate on the y axis
        range - the number of tiles away that the sound can be heard from
        delay - the amount of frames before the sound starts playing

    playSoundEffect

    void playSoundEffect​(int id, int volume)

    Plays a sound effect, even if the player's sound effect volume is muted.

    Parameters:
        id - the ID of the sound effect - SoundEffectID
        volume - the volume to play the sound effect at, see SoundEffectVolume for values used in the settings interface. if the sound effect volume is not muted, uses the set volume

    getBufferProvider

    BufferProvider getBufferProvider()

    Gets the clients graphic buffer provider.

    Returns:
        the buffer provider

    getMouseIdleTicks

    int getMouseIdleTicks()

    Gets the amount of client ticks since the last mouse movement occurred.

    Returns:
        amount of idle mouse ticks
    See Also:
        Constants.CLIENT_TICK_LENGTH

    getMouseLastPressedMillis

    long getMouseLastPressedMillis()

    Gets the time at which the last mouse press occurred in milliseconds since the UNIX epoch.
    getKeyboardIdleTicks

    int getKeyboardIdleTicks()

    Gets the amount of client ticks since the last keyboard press occurred.

    Returns:
        amount of idle keyboard ticks
    See Also:
        Constants.CLIENT_TICK_LENGTH

    changeMemoryMode

    void changeMemoryMode​(boolean lowMemory)

    Changes how game behaves based on memory mode. Low memory mode skips drawing of all floors and renders ground textures in low quality.

    Parameters:
        lowMemory - if we are running in low memory mode or not

    getItemContainer

    @Nullable ItemContainer getItemContainer​(InventoryID inventory)

    Get the item container for an inventory.

    Parameters:
        inventory - the inventory type
    Returns:
        the item container
    See Also:
        InventoryID

    getItemContainer

    @Nullable ItemContainer getItemContainer​(int id)

    Get an item container by id

    Parameters:
        id - the inventory id
    Returns:
        the item container
    See Also:
        InventoryID

    getItemContainers

    HashTable<ItemContainer> getItemContainers()

    Get all item containers

    Returns:

    getIntStackSize

    int getIntStackSize()

    Gets the length of the cs2 vm's int stack
    setIntStackSize

    void setIntStackSize​(int stackSize)

    Sets the length of the cs2 vm's int stack
    getIntStack

    int[] getIntStack()

    Gets the cs2 vm's int stack
    getStringStackSize

    int getStringStackSize()

    Gets the length of the cs2 vm's string stack
    setStringStackSize

    void setStringStackSize​(int stackSize)

    Sets the length of the cs2 vm's string stack
    getStringStack

    String[] getStringStack()

    Gets the cs2 vm's string stack
    getArraySizes

    int getArraySizes​(int arrayId)

    Get the size of one of the cs2 vm's arrays.

    Parameters:
        arrayId - the array id
    Returns:

    getArray

    int[] getArray​(int arrayId)

    Get one of the cs2 vm's arrays. Use getArraySizes(int) to get the array length.

    Parameters:
        arrayId - the array id
    Returns:

    getScriptActiveWidget

    Widget getScriptActiveWidget()

    Gets the cs2 vm's active widget This is used for all cc_* operations with a 0 operand
    getScriptDotWidget

    Widget getScriptDotWidget()

    Gets the cs2 vm's "dot" widget This is used for all .cc_* operations with a 1 operand
    isFriended

    boolean isFriended​(String name, boolean mustBeLoggedIn)

    Checks whether a player is on the friends list.

    Parameters:
        name - the name of the player
        mustBeLoggedIn - if they player is online
    Returns:
        true if the player is friends

    getFriendsChatManager

    @Nullable FriendsChatManager getFriendsChatManager()

    Retrieve the friends chat manager

    Returns:

    getFriendContainer

    FriendContainer getFriendContainer()

    Retrieve the nameable container containing friends

    Returns:

    getIgnoreContainer

    NameableContainer<Ignore> getIgnoreContainer()

    Retrieve the nameable container containing ignores

    Returns:

    getPreferences

    Preferences getPreferences()

    Gets the clients saved preferences.

    Returns:
        the client preferences

    getCameraYawTarget

    int getCameraYawTarget()

    Get the target camera yaw. The target yaw is the yaw the camera should use based on player input. The actual camera yaw, from getCameraYaw(), is what the camera is actually using, which can be overridden by eg. cutscenes.

    Returns:
        the target camera yaw

    getCameraPitchTarget

    int getCameraPitchTarget()

    Get the target camera pitch The target pitch is the pitch the camera should use based on player input. The actual camera pitch, from getCameraPitch() ()}, is what the camera is actually using, which can be overridden by eg. cutscenes.

    Returns:
        the target camera pitch

    setCameraYawTarget

    void setCameraYawTarget​(int cameraYawTarget)

    Set the target camera yaw

    Parameters:
        cameraYawTarget - target camera yaw

    setCameraPitchTarget

    void setCameraPitchTarget​(int cameraPitchTarget)

    Set the target camera pitch

    Parameters:
        cameraPitchTarget - target camera pitch

    setCameraSpeed

    void setCameraSpeed​(float speed)

    Sets the camera speed

    Parameters:
        speed - 

    setCameraMouseButtonMask

    void setCameraMouseButtonMask​(int mask)

    Sets the mask for which mouse buttons control the camera. Use 0 for the default behavior of mouse button 4 if "middle mouse moves camera" is on.

    Parameters:
        mask - 

    setCameraPitchRelaxerEnabled

    void setCameraPitchRelaxerEnabled​(boolean enabled)

    Sets whether the camera pitch can exceed the normal limits set by the RuneScape client.

    Parameters:
        enabled - new camera pitch relaxer value

    setInvertYaw

    void setInvertYaw​(boolean invertYaw)

    Sets if the moving the camera horizontally should be backwards
    setInvertPitch

    void setInvertPitch​(boolean invertPitch)

    Sets if the moving the camera vertically should be backwards
    getRenderOverview

    @Deprecated RenderOverview getRenderOverview()

    Deprecated.
    Gets the world map overview.

    Returns:
        the world map overview
    See Also:
        getWorldMap()

    getWorldMap

    WorldMap getWorldMap()

    Get the world map
    isStretchedEnabled

    boolean isStretchedEnabled()

    Checks whether the client is in stretched mode.

    Returns:
        true if the client is in stretched mode, false otherwise

    setStretchedEnabled

    void setStretchedEnabled​(boolean state)

    Sets the client stretched mode state.

    Parameters:
        state - new stretched mode state

    isStretchedFast

    boolean isStretchedFast()

    Checks whether the client is using fast rendering techniques when stretching the canvas.

    Returns:
        true if stretching is fast rendering, false otherwise

    setStretchedFast

    void setStretchedFast​(boolean state)

    Sets whether to use fast rendering techniques when stretching the canvas.

    Parameters:
        state - new fast rendering state

    setStretchedIntegerScaling

    void setStretchedIntegerScaling​(boolean state)

    Sets whether to force integer scale factor by rounding scale factors towards zero when stretching.

    Parameters:
        state - new integer scaling state

    setStretchedKeepAspectRatio

    void setStretchedKeepAspectRatio​(boolean state)

    Sets whether to keep aspect ratio when stretching.

    Parameters:
        state - new keep aspect ratio state

    setScalingFactor

    void setScalingFactor​(int factor)

    Sets the scaling factor when scaling resizable mode.

    Parameters:
        factor - new scaling factor

    invalidateStretching

    void invalidateStretching​(boolean resize)

    Invalidates cached dimensions that are used for stretching and scaling.

    Parameters:
        resize - true to tell the game to resize the canvas on the next frame, false otherwise.

    getStretchedDimensions

    Dimension getStretchedDimensions()

    Gets the current stretched dimensions of the client.

    Returns:
        the stretched dimensions

    getRealDimensions

    Dimension getRealDimensions()

    Gets the real dimensions of the client before being stretched.

    Returns:
        the real dimensions

    changeWorld

    void changeWorld​(World world)

    Changes the selected world to log in to.

    Note: this method will have no effect unless GameState is GameState.LOGIN_SCREEN.

    Parameters:
        world - the world to switch to

    createWorld

    World createWorld()

    Creates a new instance of a world.
    drawInstanceMap

    SpritePixels drawInstanceMap​(int z)

    Draws an instance map for the current viewed plane.

    Parameters:
        z - the plane
    Returns:
        the map sprite

    runScript

    void runScript​(Object... args)

    Executes a client script from the cache This method must be ran on the client thread and is not reentrant This method is shorthand for client.createScriptEvent(args).run()

    Parameters:
        args - the script id, then any additional arguments to execute the script with
    See Also:
        ScriptID

    createScriptEvent

    ScriptEvent createScriptEvent​(Object... args)

    Creates a blank ScriptEvent for executing a ClientScript2 script

    Parameters:
        args - the script id, then any additional arguments to execute the script with
    See Also:
        ScriptID

    hasHintArrow

    boolean hasHintArrow()

    Checks whether or not there is any active hint arrow.

    Returns:
        true if there is a hint arrow, false otherwise

    getHintArrowType

    int getHintArrowType()

    Gets the type of hint arrow currently displayed.

    Returns:
        the hint arrow type

    clearHintArrow

    void clearHintArrow()

    Clears the current hint arrow.
    setHintArrow

    void setHintArrow​(WorldPoint point)

    Sets a hint arrow to point to the passed location.

    Parameters:
        point - the location

    setHintArrow

    void setHintArrow​(LocalPoint point)

    Sets the hint arrow to the passsed point

    Parameters:
        point - 

    setHintArrow

    void setHintArrow​(Player player)

    Sets a hint arrow to point to the passed player.

    Parameters:
        player - the player

    setHintArrow

    void setHintArrow​(NPC npc)

    Sets a hint arrow to point to the passed NPC.

    Parameters:
        npc - the NPC

    getHintArrowPoint

    WorldPoint getHintArrowPoint()

    Gets the world point that the hint arrow is directed at.

    Returns:
        hint arrow target

    getHintArrowPlayer

    Player getHintArrowPlayer()

    Gets the player that the hint arrow is directed at.

    Returns:
        hint arrow target

    getHintArrowNpc

    NPC getHintArrowNpc()

    Gets the NPC that the hint arrow is directed at.

    Returns:
        hint arrow target

    isInterpolatePlayerAnimations

    boolean isInterpolatePlayerAnimations()

    Checks whether animation smoothing is enabled for players.

    Returns:
        true if player animation smoothing is enabled, false otherwise

    setInterpolatePlayerAnimations

    void setInterpolatePlayerAnimations​(boolean interpolate)

    Sets the animation smoothing state for players.

    Parameters:
        interpolate - the new smoothing state

    isInterpolateNpcAnimations

    boolean isInterpolateNpcAnimations()

    Checks whether animation smoothing is enabled for NPC.

    Returns:
        true if NPC animation smoothing is enabled, false otherwise

    setInterpolateNpcAnimations

    void setInterpolateNpcAnimations​(boolean interpolate)

    Sets the animation smoothing state for NPCs.

    Parameters:
        interpolate - the new smoothing state

    isInterpolateObjectAnimations

    boolean isInterpolateObjectAnimations()

    Checks whether animation smoothing is enabled for objects.

    Returns:
        true if object animation smoothing is enabled, false otherwise

    setInterpolateObjectAnimations

    void setInterpolateObjectAnimations​(boolean interpolate)

    Sets the animation smoothing state for objects.

    Parameters:
        interpolate - the new smoothing state

    getBoostedSkillLevels

    @VisibleForDevtools int[] getBoostedSkillLevels()

    getRealSkillLevels

    @VisibleForDevtools int[] getRealSkillLevels()

    getSkillExperiences

    @VisibleForDevtools int[] getSkillExperiences()

    queueChangedSkill

    void queueChangedSkill​(Skill skill)

    getSpriteOverrides

    Map<Integer,​SpritePixels> getSpriteOverrides()

    Gets a mapping of sprites to override.

    The key value in the map corresponds to the ID of the sprite, and the value the sprite to replace it with.
    getWidgetSpriteOverrides

    Map<Integer,​SpritePixels> getWidgetSpriteOverrides()

    Gets a mapping of widget sprites to override.

    The key value in the map corresponds to the packed widget ID, and the value the sprite to replace the widgets sprite with.
    setCompass

    void setCompass​(SpritePixels spritePixels)

    Sets the compass sprite.

    Parameters:
        spritePixels - the new sprite

    getWidgetSpriteCache

    NodeCache getWidgetSpriteCache()

    Returns widget sprite cache, to be used with getSpriteOverrides()

    Returns:
        the cache

    getTickCount

    int getTickCount()

    Gets the current server tick count.

    Returns:
        the tick count

    setTickCount

    void setTickCount​(int tickCount)

    Sets the current server tick count.

    Parameters:
        tickCount - the new tick count

    setInventoryDragDelay

    @Deprecated void setInventoryDragDelay​(int delay)

    Deprecated.
    Sets the inventory drag delay in client game cycles (20ms).

    Parameters:
        delay - the number of game cycles to delay dragging

    getWorldType

    EnumSet<WorldType> getWorldType()

    Gets a set of current world types that apply to the logged in world.

    Returns:
        the types for current world

    getCameraMode

    int getCameraMode()

    Get the camera mode

    Returns:
        0 for normal, 1 for free camera

    setCameraMode

    void setCameraMode​(int mode)

    Set the camera mode

    Parameters:
        mode - 0 for normal, 1 for free camera

    getCameraFocalPointX

    double getCameraFocalPointX()

    Get the camera focus point x Typically this is the player position, but can be other points in cutscenes or in free camera mode.

    Returns:

    setCameraFocalPointX

    void setCameraFocalPointX​(double x)

    Sets the camera focus point x. Requires the getCameraMode() to be free camera.

    Parameters:
        x - 

    getCameraFocalPointY

    double getCameraFocalPointY()

    Get the camera focus point y Typically this is the player position, but can be other points in cutscenes or in free camera mode.

    Returns:

    setCameraFocalPointY

    void setCameraFocalPointY​(double y)

    Sets the camera focus point y. Requires the getCameraMode() to be free camera.

    Parameters:
        y - 

    getCameraFocalPointZ

    double getCameraFocalPointZ()

    Get the camera focus point z Typically this is the player position, but can be other points in cutscenes or in free camera mode.

    Returns:

    setCameraFocalPointZ

    void setCameraFocalPointZ​(double z)

    Sets the camera focus point z. Requires the getCameraMode() to be free camera.

    Parameters:
        z - 

    setFreeCameraSpeed

    void setFreeCameraSpeed​(int speed)

    Sets the normal moving speed when using oculus orb (default value is 12)
    getOculusOrbState

    @Deprecated int getOculusOrbState()

    Deprecated.
    Gets the enabled state for the Oculus orb mode
    setOculusOrbState

    @Deprecated void setOculusOrbState​(int state)

    Deprecated.
    Sets the enabled state for the Oculus orb state

    Parameters:
        state - boolean enabled value

    setOculusOrbNormalSpeed

    @Deprecated void setOculusOrbNormalSpeed​(int speed)

    Deprecated.
    Sets the normal moving speed when using oculus orb (default value is 12)
    getOculusOrbFocalPointX

    @Deprecated int getOculusOrbFocalPointX()

    Deprecated.
    Gets local X coord where the camera is pointing when the Oculus orb is active
    getOculusOrbFocalPointY

    @Deprecated int getOculusOrbFocalPointY()

    Deprecated.
    Gets local Y coord where the camera is pointing when the Oculus orb is active
    openWorldHopper

    void openWorldHopper()

    Opens in-game world hopper interface
    hopToWorld

    void hopToWorld​(World world)

    Hops using in-game world hopper widget to another world

    Parameters:
        world - target world to hop to

    setSkyboxColor

    void setSkyboxColor​(int skyboxColor)

    Sets the RGB color of the skybox
    getSkyboxColor

    int getSkyboxColor()

    Gets the RGB color of the skybox
    isGpu

    boolean isGpu()

    setGpuFlags

    void setGpuFlags​(int gpuflags)

    setExpandedMapLoading

    void setExpandedMapLoading​(int chunks)

    getExpandedMapLoading

    int getExpandedMapLoading()

    get3dZoom

    int get3dZoom()

    getCenterX

    int getCenterX()

    getCenterY

    int getCenterY()

    getTextureProvider

    TextureProvider getTextureProvider()

    getRasterizer3D_clipMidX2

    int getRasterizer3D_clipMidX2()

    getRasterizer3D_clipNegativeMidX

    int getRasterizer3D_clipNegativeMidX()

    getRasterizer3D_clipNegativeMidY

    int getRasterizer3D_clipNegativeMidY()

    getRasterizer3D_clipMidY2

    int getRasterizer3D_clipMidY2()

    checkClickbox

    void checkClickbox​(Projection projection, Model model, int orientation, int x, int y, int z, long hash)

    isWidgetSelected

    boolean isWidgetSelected()

    Is a widget is in target mode?
    setWidgetSelected

    void setWidgetSelected​(boolean selected)

    Sets if a widget is in target mode
    getSelectedWidget

    @Nullable Widget getSelectedWidget()

    Get the selected widget, such as a selected spell or selected item (eg. "Use")

    Returns:
        the selected widget

    getItemCompositionCache

    NodeCache getItemCompositionCache()

    Returns client item composition cache
    getObjectCompositionCache

    NodeCache getObjectCompositionCache()

    Returns client object composition cache

    Returns:

    getAnimationCache

    NodeCache getAnimationCache()

    Returns the client Animation cache
    getCrossSprites

    SpritePixels[] getCrossSprites()

    Returns the array of cross sprites that appear and animate when left-clicking
    getEnum

    EnumComposition getEnum​(int id)

    draw2010Menu

    void draw2010Menu​(int alpha)

    Draws a menu in the 2010 interface style.

    Parameters:
        alpha - background transparency of the menu

    drawOriginalMenu

    void drawOriginalMenu​(int alpha)

    Draws a menu in the OSRS interface style.

    Parameters:
        alpha - background transparency of the menu

    resetHealthBarCaches

    void resetHealthBarCaches()

    getItemCount

    int getItemCount()

    Returns the max item index + 1 from cache
    setAllWidgetsAreOpTargetable

    void setAllWidgetsAreOpTargetable​(boolean value)

    Makes all widgets behave as if they are WidgetConfig.WIDGET_USE_TARGET
    setGeSearchResultCount

    void setGeSearchResultCount​(int count)

    Sets the result count for GE search
    setGeSearchResultIds

    void setGeSearchResultIds​(short[] ids)

    Sets the array of item ids for GE search
    setGeSearchResultIndex

    void setGeSearchResultIndex​(int index)

    Sets the starting index in the item id array for GE search
    setLoginScreen

    void setLoginScreen​(SpritePixels pixels)

    Sets the image to be used for the login screen, provided as SpritePixels If the image is larger than half the width of fixed mode, it won't get mirrored to the other side of the screen
    setShouldRenderLoginScreenFire

    void setShouldRenderLoginScreenFire​(boolean val)

    Sets whether the flames on the login screen should be rendered
    isKeyPressed

    boolean isKeyPressed​(int keycode)

    Test if a key is pressed

    Parameters:
        keycode - the keycode
    Returns:
    See Also:
        KeyCode

    getCrossWorldMessageIds

    long[] getCrossWorldMessageIds()

    Get the list of message ids for the recently received cross-world messages. The upper 32 bits of the id is the world id, the lower is a sequence number per-world.

    Returns:

    getCrossWorldMessageIdsIndex

    int getCrossWorldMessageIdsIndex()

    Get the index of the next message to be inserted in the cross world message id list

    Returns:

    getClanChannel

    @Nullable ClanChannel getClanChannel()

    Get the primary clan channel the player is in.

    Returns:

    getGuestClanChannel

    @Nullable ClanChannel getGuestClanChannel()

    Get the guest clan channel the player is in.

    Returns:

    getClanSettings

    @Nullable ClanSettings getClanSettings()

    Get clan settings for the clan the user is in.

    Returns:

    getGuestClanSettings

    @Nullable ClanSettings getGuestClanSettings()

    Get the guest clan's settings.

    Returns:

    getClanChannel

    @Nullable ClanChannel getClanChannel​(int clanId)

    Get clan channel by id.

    Parameters:
        clanId - the clan id
    Returns:
    See Also:
        ClanID

    getClanSettings

    @Nullable ClanSettings getClanSettings​(int clanId)

    Get clan settings by id

    Parameters:
        clanId - the clan id
    Returns:
    See Also:
        ClanID

    setUnlockedFps

    void setUnlockedFps​(boolean unlock)

    setUnlockedFpsTarget

    void setUnlockedFpsTarget​(int fps)

    getAmbientSoundEffects

    Deque<AmbientSoundEffect> getAmbientSoundEffects()

    Gets the ambient sound effects

    Returns:

    setIdleTimeout

    void setIdleTimeout​(int ticks)

    Set the amount of time until the client automatically logs out due to idle input.

    Parameters:
        ticks - client ticks

    getIdleTimeout

    int getIdleTimeout()

    Get the amount of time until the client automatically logs out due to idle input.

    Returns:
        client ticks

    isMinimapZoom

    boolean isMinimapZoom()

    Get whether minimap zoom is enabled

    Returns:

    setMinimapZoom

    void setMinimapZoom​(boolean minimapZoom)

    Set whether minimap zoom is enabled

    Parameters:
        minimapZoom - 

    getMinimapZoom

    double getMinimapZoom()

    Gets the number of pixels per tile on the minimap. The default is 4.

    Returns:

    setMinimapZoom

    void setMinimapZoom​(double zoom)

    Set the number of pixels per tile on the minimap. The default is 4.

    Parameters:
        zoom - 

    setMinimapTileDrawer

    void setMinimapTileDrawer​(TileFunction drawTile)

    Sets a callback to override the drawing of tiles on the minimap. Will be called per tile per frame.
    getRasterizer

    Rasterizer getRasterizer()

    menuAction

    void menuAction​(int p0, int p1, MenuAction action, int id, int itemId, String option, String target)

    getWorldView

    WorldView getWorldView​(int id)

    Get worldview by id

    Parameters:
        id - id, or -1 for top level worldview
    Returns:

    getTopLevelWorldView

    WorldView getTopLevelWorldView()

    Get the top level world view

    Returns:

    getInstanceTemplateChunks

    @Deprecated int[][][] getInstanceTemplateChunks()

    Deprecated.
    Contains a 3D array of template chunks for instanced areas.

    The array returned is of format [z][x][y], where z is the plane, x and y the x-axis and y-axis coordinates of a tile divided by the size of a chunk.

    The bits of the int value held by the coordinates are -1 if there is no data, structured in the following format:


        0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | |rot|     y chunk coord     |    x chunk coord    |pln|       |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        

    Returns:
        the array of instance template chunks
    See Also:
        Constants.CHUNK_SIZE, InstanceTemplates

    getXteaKeys

    @Deprecated int[][] getXteaKeys()

    Deprecated.
    Returns a 2D array containing XTEA encryption keys used to decrypt map region files.

    The array maps the region keys at index n to the region ID held in getMapRegions() at n.

    The array of keys for the region make up a 128-bit encryption key spread across 4 integers.

    Returns:
        the XTEA encryption keys

    isInInstancedRegion

    @Deprecated boolean isInInstancedRegion()

    Deprecated.
    Checks whether the scene is in an instanced region.
    getMapRegions

    @Deprecated int[] getMapRegions()

    Deprecated.
    Gets an array of map region IDs that are currently loaded.

    Returns:
        the map regions

    getScene

    @Deprecated default Scene getScene()

    Deprecated.
    Gets the current scene
    getPlayers

    @Deprecated default List<Player> getPlayers()

    Deprecated.
    Gets a list of all valid players from the player cache.

    Returns:
        a list of all players

    getNpcs

    @Deprecated default List<NPC> getNpcs()

    Deprecated.
    Gets a list of all valid NPCs from the NPC cache.

    Returns:
        a list of all NPCs

    getCachedNPCs

    @Deprecated default NPC[] getCachedNPCs()

    Deprecated.
    Gets an array of all cached NPCs.

    Returns:
        cached NPCs

    getCachedPlayers

    @Deprecated default Player[] getCachedPlayers()

    Deprecated.
    Gets an array of all cached players.

    Returns:
        cached players

    getCollisionMaps

    @Nullable @Deprecated default CollisionData[] getCollisionMaps()

    Deprecated.
    Gets an array of tile collision data.

    The index into the array is the plane/z-axis coordinate.

    Returns:
        the collision data

    getPlane

    @Deprecated default int getPlane()

    Deprecated.
    Gets the current plane the player is on.

    This value indicates the current map level above ground level, where ground level is 0. For example, going up a ladder in Lumbridge castle will put the player on plane 1.

    Note: This value will never be below 0. Basements and caves below ground level use a tile offset and are still considered plane 0 by the game.

    Returns:
        the plane

    getTileHeights

    @Deprecated default int[][][] getTileHeights()

    Deprecated.
    Gets a 3D array containing the heights of tiles in the current scene.

    Returns:
        the tile heights

    getTileSettings

    @Deprecated default byte[][][] getTileSettings()

    Deprecated.
    Gets a 3D array containing the settings of tiles in the current scene.

    Returns:
        the tile settings

    getBaseX

    @Deprecated default int getBaseX()

    Deprecated.
    Returns the x-axis base coordinate.

    This value is the x-axis world coordinate of tile (0, 0) in the current scene (ie. the bottom-left most coordinates in the scene).

    Returns:
        the base x-axis coordinate

    getBaseY

    @Deprecated default int getBaseY()

    Deprecated.
    Returns the y-axis base coordinate.

    This value is the y-axis world coordinate of tile (0, 0) in the current scene (ie. the bottom-left most coordinates in the scene).

    Returns:
        the base y-axis coordinate

    createProjectile

    @Deprecated default Projectile createProjectile​(int id, int plane, int startX, int startY, int startZ, int startCycle, int endCycle, int slope, int startHeight, int endHeight, @Nullable Actor target, int targetX, int targetY)

    Deprecated.
    Create a projectile.

    Parameters:
        id - projectile/spotanim id
        plane - plane the projectile is on
        startX - local x coordinate the projectile starts at
        startY - local y coordinate the projectile starts at
        startZ - local z coordinate the projectile starts at - includes tile height
        startCycle - cycle the project starts
        endCycle - cycle the projectile ends
        slope - 
        startHeight - start height of projectile - excludes tile height
        endHeight - end height of projectile - excludes tile height
        target - optional actor target
        targetX - target x - if an actor target is supplied should be the target x
        targetY - target y - if an actor target is supplied should be the target y
    Returns:
        the new projectile

    getProjectiles

    @Deprecated default Deque<Projectile> getProjectiles()

    Deprecated.
    Gets a list of all projectiles currently spawned.

    Returns:
        all projectiles

    getGraphicsObjects

    @Deprecated default Deque<GraphicsObject> getGraphicsObjects()

    Deprecated.
    Gets a list of all graphics objects currently drawn.

    Returns:
        all graphics objects

    getSelectedSceneTile

    @Deprecated @Nullable default Tile getSelectedSceneTile()

    Deprecated.
    Gets the currently selected tile. (ie. last right clicked tile)

    Returns:
        the selected tile

Skip navigation links

Overview
Package
Class
Use
Tree
Deprecated
Index
Help

All Classes

Summary: 
Nested | 
Field | 
Constr | 
Method

Detail: 
Field | 
Constr | 
Method

Copyright © 2014–1970. All rights reserved.
No search results. 
