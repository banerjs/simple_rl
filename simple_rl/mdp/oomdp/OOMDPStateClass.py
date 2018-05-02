''' OOMDPStateClass.py: Contains the OOMDP State Class. '''

# Python imports.
from __future__ import print_function

# Other imports.
from simple_rl.mdp.StateClass import State

class OOMDPState(State):
    ''' OOMDP State class '''

    def __init__(self, objects):
        '''
        Args:
            objects (dict of OOMDPObject instances): {key=object class (str):val = object instances}
        '''
        self.objects = objects
        self.object_keys = sorted(self.objects.keys())
        self.data = None
        self.update()

        State.__init__(self, data=self.data)

    def get_objects(self):
        return self.objects

    def get_objects_of_class(self, obj_class):
        try:
            return self.objects[obj_class]
        except KeyError:
            raise ValueError("Error: given object class (" + str(obj_class) + ") not found in state.\n\t Known classes are: ", self.objects.keys())

    def get_first_obj_of_class(self, obj_class):
        return self.get_objects_of_class(obj_class)[0]

    def get_feature_indices(self):
        return self.feature_indices

    def update(self):
        '''
        Summary:
            Turn object attributes into a feature list.
        '''

        self.feature_indices = {} if self.data is None else self.feature_indices
        state_vec = [] if self.data is None else list(self.data)

        feature_index = -1
        for obj_class in self.object_keys:

            for oidx, obj in enumerate(self.objects[obj_class]):
                obj_state = obj.get_obj_state()

                # Set the position of the different objects
                for aidx, attr in enumerate(obj.get_attribute_keys()):
                    feature_index += 1
                    if self.data is None:
                        state_vec.append(obj_state[aidx])
                        self.feature_indices["{}-{}-{}".format(obj_class, oidx, attr)] = feature_index
                    else:
                        state_vec[feature_index] = obj_state[aidx]

        self.data = tuple(state_vec)


    def __str__(self):
        result = ""
        for obj_class in self.object_keys:
            for obj in self.objects[obj_class]:
                result += "\t" + str(obj)
            result += "\n"
        return result
