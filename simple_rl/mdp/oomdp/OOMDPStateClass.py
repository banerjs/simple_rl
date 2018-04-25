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
        self.object_keys = sorted(self.objects.keys())
        self.feature_indices = {}

        state_vec = []
        feature_index = -1
        for obj_class in self.object_keys:

            for obj in self.objects[obj_class]:
                state_vec += obj.get_obj_state()

                # Set the position of the different objects
                for attr in obj.get_attribute_keys():
                    feature_index += 1
                    self.feature_indices["{}-{}".format(obj_class, attr)] = feature_index

        self.data = tuple(state_vec)

    def __str__(self):
        result = ""
        for obj_class in self.object_keys:
            for obj in self.objects[obj_class]:
                result += "\t" + str(obj)
            result += "\n"
        return result
